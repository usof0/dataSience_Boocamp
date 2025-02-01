#!/bin/sh

OUTPUT_CSV="hh_concatenator.csv"

FILES=$(ls | grep -E '^[0-9]{4}-[0-9]{2}-[0-9]{2}\.csv$')

head -n 1 $(echo "$FILES" | head -n 1) > "$OUTPUT_CSV"

for file in $FILES; do
    tail -n +2 $file >> $OUTPUT_CSV
done

echo "Concatenated CSV file saved to $OUTPUT_CSV"