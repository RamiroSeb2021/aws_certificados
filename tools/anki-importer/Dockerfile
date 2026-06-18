FROM python:3.12.11-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:0.8.15 /uv /uvx /bin/

WORKDIR /work

COPY pyproject.toml uv.lock /app/
COPY import_anki_csv.py /app/import_anki_csv.py

ENTRYPOINT ["uv", "run", "--project", "/app", "--locked", "--no-sync", "python", "/app/import_anki_csv.py"]
