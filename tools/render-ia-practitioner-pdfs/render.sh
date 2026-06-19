#!/bin/sh
set -eu

notes_dir="${NOTES_DIR:-/work/IA_practitioner/notes}"
output_dir="${OUTPUT_DIR:-/work/IA_practitioner/rendered-pdfs}"

mkdir -p "$output_dir"

set -- "$notes_dir"/*.md
if [ ! -e "$1" ]; then
  printf 'No Markdown notes found in %s\n' "$notes_dir" >&2
  exit 1
fi

count=0
failures=0

for note do
  base="$(basename "$note" .md)"
  output="$output_dir/$base.pdf"
  count=$((count + 1))

  printf 'Rendering %s -> %s\n' "$note" "$output"

  if ! pandoc "$note" \
    --from=gfm \
    --standalone \
    --pdf-engine=xelatex \
    --variable=mainfont:'DejaVu Serif' \
    --variable=monofont:'DejaVu Sans Mono' \
    --variable=geometry:margin=1in \
    --metadata "title=$base" \
    --output="$output"; then
    printf 'Failed: %s\n' "$note" >&2
    failures=$((failures + 1))
  fi
done

if [ "$failures" -gt 0 ]; then
  printf '%s render failure(s).\n' "$failures" >&2
  exit 1
fi

printf 'Rendered %s PDF(s) into %s using pandoc with xelatex.\n' "$count" "$output_dir"
