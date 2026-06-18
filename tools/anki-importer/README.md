# Anki CSV Importer

Docker-based importer for `IA_practitioner/IA Practitioner.csv` using AnkiConnect.

This tool is dry-run first. It validates and summarizes the CSV by default; it only writes to Anki when `--import` is passed.

## Requirements

- Anki Desktop running on the host.
- AnkiConnect add-on installed and listening on port `8765`.
- Docker available for the isolated runner.

The default AnkiConnect URL is `http://host.docker.internal:8765`. Override it with `--anki-url` or `ANKI_CONNECT_URL`.

If your AnkiConnect configuration requires an API key, pass `--anki-api-key` or set `ANKI_CONNECT_API_KEY`.

## Mapping

| CSV column | Anki mapping |
|---|---|
| `Deck` | Anki deck name, unless `--deck` overrides it |
| `Topic` | Preserved in `Back` for Basic notes and `Back Extra` for Cloze notes |
| `Front` | `Front` for Basic notes; `Text` for Cloze notes |
| `Back` | `Back` for Basic notes; included in `Back Extra` for Cloze if present |
| `Type=basic` | Anki `Basic` note type |
| `Type=scenario` | Anki `Basic` note type |
| `Type=cloze` | Anki `Cloze` note type |
| `Tags` | Split on whitespace and sent as Anki tags |
| `Caveat` | Preserved in `Back` or `Back Extra` |

Duplicates are not overwritten. The importer sends `allowDuplicate: false` to AnkiConnect.

## Build

From the repository root:

```bash
docker build -t aws-anki-importer tools/anki-importer
```

## Dry Run

```bash
docker run --rm \
  -v "$PWD:/work:ro" \
  aws-anki-importer
```

This validates `IA_practitioner/IA Practitioner.csv`, prints counts by card type/model/deck, and shows sample payload summaries.

## Import

```bash
docker run --rm \
  -v "$PWD:/work:ro" \
  aws-anki-importer --import
```

Override the deck name:

```bash
docker run --rm \
  -v "$PWD:/work:ro" \
  aws-anki-importer --deck "IA Practitioner" --import
```

## Linux Host Networking

If `host.docker.internal` does not resolve on Linux, use host networking:

```bash
docker run --rm --network host \
  -v "$PWD:/work:ro" \
  -e ANKI_CONNECT_URL="http://127.0.0.1:8765" \
  aws-anki-importer --import
```

Alternatively, add Docker's host gateway mapping:

```bash
docker run --rm \
  --add-host=host.docker.internal:host-gateway \
  -v "$PWD:/work:ro" \
  aws-anki-importer --import
```

## Local Syntax Check

No host dependency install is required. If Python 3.12+ is available on the host:

```bash
python3 -m py_compile tools/anki-importer/import_anki_csv.py
python3 tools/anki-importer/import_anki_csv.py
```

## AnkiConnect API Notes

- Requests are JSON POSTs with `action`, `version`, and `params`.
- `createDeck` creates the deck if needed and is safe to call for an existing deck.
- `addNotes` accepts a list of note payloads.
- Basic notes use model `Basic` with fields `Front` and `Back`.
- Cloze notes use model `Cloze` with fields `Text` and `Back Extra`.
- Tags are sent as a list of strings in the note payload.
- Duplicate protection is controlled with `options.allowDuplicate: false`.
- If configured, AnkiConnect API keys are sent as the top-level `key` property.
