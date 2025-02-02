#!/bin/bash

# Find all .out files recursively and process them
find . -type f -name "*.out" | while read file; do
    echo "Processing: $file"
    temp_file="${file}.tmp"
    cat "$file" | tr -s '\r\n' > "$temp_file"
    mv "$temp_file" "$file"
done