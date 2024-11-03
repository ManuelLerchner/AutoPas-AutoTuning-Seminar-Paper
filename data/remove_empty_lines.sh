#!/bin/bash

# Find all .out files recursively and process them
find . -type f -name "*.out" | while read file; do
    echo "Processing: $file"
    # Create temporary file in the same directory as the original file
    temp_file="${file}.tmp"
    # Remove empty lines and write to temp file
    cat "$file" | tr -s '\r\n' > "$temp_file"
    # Replace original with processed file
    mv "$temp_file" "$file"
done