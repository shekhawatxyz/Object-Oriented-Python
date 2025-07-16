#!/bin/zsh

echo "Adding .gitkeep files to empty directories..."

for dir in Chapter-*-*; do
  if [[ -d "$dir" && -z "$(ls -A "$dir")" ]]; then
    touch "${dir}/.gitkeep"
    echo "Added .gitkeep to: $dir"
  fi
done

echo ""
echo "Finished adding .gitkeep files."
