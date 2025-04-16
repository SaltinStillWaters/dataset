#!/bin/bash

# Usage: ./replace_equals.sh filename.txt

file="$1"

if [[ -z "$file" ]]; then
  echo "Usage: $0 filename.txt"
  exit 1
fi

# In-place replacement
sed -i -e 's/\bis equal to\b/=/gI' \
       -e 's/\bequal to\b/=/gI' \
       -e 's/\bequals\b/=/gI' \
       -e 's/\bequal\b/=/gI' "$file"
