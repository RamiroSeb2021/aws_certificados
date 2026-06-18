#!/usr/bin/env python3
"""Import the AI Practitioner CSV into Anki through AnkiConnect.

Dry-run is the default. Use --import to write notes.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import os
import re
import sys
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any


ANKI_CONNECT_VERSION = 6
DEFAULT_ANKI_URL = "http://host.docker.internal:8765"
DEFAULT_CSV = Path("IA_practitioner/IA Practitioner.csv")
REQUIRED_HEADERS = ["Deck", "Topic", "Front", "Back", "Type", "Tags", "Caveat"]
SUPPORTED_TYPES = {"basic", "scenario", "cloze"}
CLOZE_PATTERN = re.compile(r"{{c\d+::.+?}}")


class ImporterError(Exception):
    """Raised for expected validation or AnkiConnect errors."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate or import an Anki CSV with Basic and Cloze note mapping."
    )
    parser.add_argument("csv_path", nargs="?", type=Path, default=DEFAULT_CSV)
    parser.add_argument(
        "--deck",
        help="Override the deck name from the CSV Deck column for every note.",
    )
    parser.add_argument(
        "--anki-url",
        default=os.environ.get("ANKI_CONNECT_URL", DEFAULT_ANKI_URL),
        help="AnkiConnect URL. Defaults to ANKI_CONNECT_URL or host.docker.internal:8765.",
    )
    parser.add_argument(
        "--anki-api-key",
        default=os.environ.get("ANKI_CONNECT_API_KEY"),
        help="Optional AnkiConnect API key. Defaults to ANKI_CONNECT_API_KEY.",
    )
    parser.add_argument(
        "--basic-model",
        default="Basic",
        help="Anki note type for CSV basic/scenario rows. Default: Basic.",
    )
    parser.add_argument(
        "--cloze-model",
        default="Cloze",
        help="Anki note type for CSV cloze rows. Default: Cloze.",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=50,
        help="Number of notes per AnkiConnect addNotes call. Default: 50.",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=3,
        help="Dry-run payload summaries to print. Default: 3.",
    )
    parser.add_argument(
        "--import",
        dest="do_import",
        action="store_true",
        help="Actually create the deck and add notes. Without this flag, dry-run only.",
    )
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise ImporterError(f"CSV file not found: {path}")

    with path.open(newline="", encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file)
        if reader.fieldnames != REQUIRED_HEADERS:
            raise ImporterError(
                "CSV headers must be exactly "
                f"{REQUIRED_HEADERS}; got {reader.fieldnames or []}"
            )
        return [
            {key: (value or "").strip() for key, value in row.items()} for row in reader
        ]


def validate_rows(rows: list[dict[str, str]]) -> None:
    if not rows:
        raise ImporterError("CSV has no data rows.")

    errors: list[str] = []
    for index, row in enumerate(rows, start=2):
        card_type = row["Type"].lower()
        if card_type not in SUPPORTED_TYPES:
            errors.append(f"line {index}: unsupported Type {row['Type']!r}")
        if not row["Deck"]:
            errors.append(f"line {index}: Deck is required")
        if not row["Topic"]:
            errors.append(f"line {index}: Topic is required")
        if not row["Front"]:
            errors.append(f"line {index}: Front is required")
        if card_type in {"basic", "scenario"} and not row["Back"]:
            errors.append(f"line {index}: Back is required for {card_type}")
        if card_type == "cloze" and not CLOZE_PATTERN.search(row["Front"]):
            errors.append(f"line {index}: Cloze Front must contain Anki cloze markup")

    if errors:
        shown = "\n".join(errors[:20])
        remaining = len(errors) - 20
        if remaining > 0:
            shown += f"\n... and {remaining} more errors"
        raise ImporterError(shown)


def split_tags(value: str) -> list[str]:
    return [tag for tag in value.split() if tag]


def html_paragraph(label: str, value: str) -> str:
    escaped_value = html.escape(value).replace("\n", "<br>")
    return f"<p><strong>{html.escape(label)}:</strong> {escaped_value}</p>"


def build_extra(row: dict[str, str]) -> str:
    parts: list[str] = []
    if row["Back"]:
        parts.append(html_paragraph("Back", row["Back"]))
    parts.append(html_paragraph("Topic", row["Topic"]))
    if row["Caveat"]:
        parts.append(html_paragraph("Caveat", row["Caveat"]))
    return "\n".join(parts)


def build_basic_back(row: dict[str, str]) -> str:
    parts = [html.escape(row["Back"]).replace("\n", "<br>")]
    parts.append("<hr>")
    parts.append(html_paragraph("Topic", row["Topic"]))
    if row["Caveat"]:
        parts.append(html_paragraph("Caveat", row["Caveat"]))
    return "\n".join(parts)


def build_note(
    row: dict[str, str], deck_override: str | None, basic_model: str, cloze_model: str
) -> dict[str, Any]:
    deck_name = deck_override or row["Deck"]
    card_type = row["Type"].lower()
    options = {"allowDuplicate": False}

    if card_type == "cloze":
        return {
            "deckName": deck_name,
            "modelName": cloze_model,
            "fields": {
                "Text": row["Front"],
                "Back Extra": build_extra(row),
            },
            "tags": split_tags(row["Tags"]),
            "options": options,
        }

    return {
        "deckName": deck_name,
        "modelName": basic_model,
        "fields": {
            "Front": row["Front"],
            "Back": build_basic_back(row),
        },
        "tags": split_tags(row["Tags"]),
        "options": options,
    }


def build_notes(
    args: argparse.Namespace, rows: list[dict[str, str]]
) -> list[dict[str, Any]]:
    return [
        build_note(row, args.deck, args.basic_model, args.cloze_model) for row in rows
    ]


def call_anki(
    url: str,
    action: str,
    params: dict[str, Any] | None = None,
    api_key: str | None = None,
) -> Any:
    request_payload: dict[str, Any] = {
        "action": action,
        "version": ANKI_CONNECT_VERSION,
        "params": params or {},
    }
    if api_key:
        request_payload["key"] = api_key
    payload = json.dumps(request_payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            body = response.read().decode("utf-8")
    except urllib.error.URLError as exc:
        raise ImporterError(f"Could not reach AnkiConnect at {url}: {exc}") from exc

    try:
        decoded = json.loads(body)
    except json.JSONDecodeError as exc:
        raise ImporterError(f"AnkiConnect returned invalid JSON: {body[:500]}") from exc

    if decoded.get("error"):
        raise ImporterError(f"AnkiConnect {action} failed: {decoded['error']}")
    return decoded.get("result")


def chunks(items: list[dict[str, Any]], size: int) -> list[list[dict[str, Any]]]:
    if size < 1:
        raise ImporterError("--batch-size must be at least 1")
    return [items[index : index + size] for index in range(0, len(items), size)]


def summarize_payload(note: dict[str, Any]) -> dict[str, Any]:
    fields = note["fields"]
    primary = fields.get("Front") or fields.get("Text") or ""
    return {
        "deckName": note["deckName"],
        "modelName": note["modelName"],
        "primaryField": primary[:100] + ("..." if len(primary) > 100 else ""),
        "fieldNames": list(fields),
        "tags": note["tags"],
        "allowDuplicate": note["options"]["allowDuplicate"],
    }


def print_dry_run(
    rows: list[dict[str, str]], notes: list[dict[str, Any]], sample_size: int
) -> None:
    type_counts = Counter(row["Type"].lower() for row in rows)
    model_counts = Counter(note["modelName"] for note in notes)
    deck_counts = Counter(note["deckName"] for note in notes)
    caveat_count = sum(1 for row in rows if row["Caveat"])

    print("DRY RUN: no notes were added. Use --import to write to Anki.")
    print(f"Rows: {len(rows)}")
    print(f"Types: {dict(type_counts)}")
    print(f"Models: {dict(model_counts)}")
    print(f"Decks: {dict(deck_counts)}")
    print(f"Rows with Caveat preserved: {caveat_count}")
    print("Sample payload summaries:")
    for note in notes[:sample_size]:
        print(json.dumps(summarize_payload(note), ensure_ascii=False, indent=2))


def import_notes(
    url: str, notes: list[dict[str, Any]], batch_size: int, api_key: str | None
) -> None:
    decks = sorted({note["deckName"] for note in notes})
    for deck in decks:
        deck_id = call_anki(url, "createDeck", {"deck": deck}, api_key)
        print(f"Deck ready: {deck} ({deck_id})")

    created = 0
    duplicates_or_failed = 0
    failures: list[str] = []

    for batch_number, batch in enumerate(chunks(notes, batch_size), start=1):
        try:
            result = call_anki(url, "addNotes", {"notes": batch}, api_key)
        except ImporterError as exc:
            failures.append(f"batch {batch_number}: {exc}")
            for note in batch:
                try:
                    note_id = call_anki(url, "addNote", {"note": note}, api_key)
                except ImporterError as item_exc:
                    duplicates_or_failed += 1
                    failures.append(
                        f"note {summarize_payload(note)['primaryField']!r}: {item_exc}"
                    )
                else:
                    created += 1
                    print(f"Added note {note_id}")
            continue

        if not isinstance(result, list):
            raise ImporterError(f"Unexpected addNotes result: {result!r}")
        for note, note_id in zip(batch, result, strict=True):
            if note_id is None:
                duplicates_or_failed += 1
                failures.append(
                    f"note {summarize_payload(note)['primaryField']!r}: not added; likely duplicate or empty"
                )
            else:
                created += 1
        print(f"Imported batch {batch_number}: {created} created so far")

    print(f"Created notes: {created}")
    print(f"Duplicates or failures: {duplicates_or_failed}")
    if failures:
        print("Failures:", file=sys.stderr)
        for failure in failures[:50]:
            print(f"- {failure}", file=sys.stderr)
        if len(failures) > 50:
            print(f"- ... and {len(failures) - 50} more", file=sys.stderr)


def main() -> int:
    args = parse_args()
    try:
        rows = read_rows(args.csv_path)
        validate_rows(rows)
        notes = build_notes(args, rows)
        if not args.do_import:
            print_dry_run(rows, notes, args.sample_size)
            return 0
        version = call_anki(args.anki_url, "version", api_key=args.anki_api_key)
        print(f"Connected to AnkiConnect API version: {version}")
        import_notes(args.anki_url, notes, args.batch_size, args.anki_api_key)
        return 0
    except ImporterError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
