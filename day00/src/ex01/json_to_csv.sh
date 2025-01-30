#!/bin/sh

INPUT_JSON="./../ex00/hh.json"
OUTPUT_CSV="hh.csv"

# run jq with the filter.jq file to convert JSON to CSV to CSV
jq -r -f filter.jq "$INPUT_JSON" > "$OUTPUT_CSV"

echo "CSV file saved to $OUTPUT_CSV"