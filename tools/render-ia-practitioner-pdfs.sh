#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
image="${IA_PRACTITIONER_PDF_IMAGE:-aws-certificados/ia-practitioner-pdf-renderer:local}"
dockerfile_dir="$repo_root/tools/render-ia-practitioner-pdfs"

if ! command -v docker >/dev/null 2>&1; then
  printf 'Docker is required to render IA Practitioner PDFs.\n' >&2
  exit 127
fi

docker build -t "$image" "$dockerfile_dir"

docker run --rm \
  --user "$(id -u):$(id -g)" \
  --env HOME=/tmp \
  --volume "$repo_root:/work" \
  --workdir /work \
  "$image"
