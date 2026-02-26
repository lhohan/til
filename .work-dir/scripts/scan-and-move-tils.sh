#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
DEST_DIR="${REPO_ROOT}/.work-dir/drafts"

mkdir -p "${DEST_DIR}"

candidates=()
for root in "$HOME/dev" "$HOME/dotfiles"; do
  if [ -d "${root}" ]; then
    while IFS= read -r -d '' file; do
      candidates+=("${file}")
    done < <(find "${root}" -type f -path '*/docs/tils/*.md' -print0)
  fi
done

count=${#candidates[@]}
if [ "${count}" -eq 0 ]; then
  echo "No matching files found in ~/dev or ~/dotfiles for */docs/tils/*.md"
  exit 0
fi

echo "Found ${count} matching file(s):"
for i in "${!candidates[@]}"; do
  idx=$((i + 1))
  echo "  ${idx}. ${candidates[$i]}"
done

echo
read -r -p "Move all files to ${DEST_DIR}? [y/N] " confirm
case "${confirm}" in
  [Yy]|[Yy][Ee][Ss])
    ;;
  *)
    echo "Cancelled. No files moved."
    exit 0
    ;;
esac

moved=0
renamed=0
for src in "${candidates[@]}"; do
  base_name="$(basename "${src}")"
  stem="${base_name%.*}"
  ext="${base_name##*.}"

  target="${DEST_DIR}/${base_name}"
  if [ -e "${target}" ]; then
    n=2
    while true; do
      candidate="${DEST_DIR}/${stem}-${n}.${ext}"
      if [ ! -e "${candidate}" ]; then
        target="${candidate}"
        renamed=$((renamed + 1))
        break
      fi
      n=$((n + 1))
    done
  fi

  mv "${src}" "${target}"
  moved=$((moved + 1))
  echo "Moved: ${src} -> ${target}"
done

echo
echo "Done. Found: ${count}, Moved: ${moved}, Renamed: ${renamed}"
