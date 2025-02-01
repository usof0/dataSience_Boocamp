#!/bin/sh

INPUT_CSV="../ex03/hh_positions.csv"
OUTPUT_CSV="hh_uniq_positions.csv"

echo '"name", "count"' > "$OUTPUT_CSV"
tail -n +2 "$INPUT_CSV" | awk -F, '{print $3}' | sed 's/"//g' | sort | uniq -c | sort -nr | awk '{print "\"" $2 "\"," $1}' >> "$OUTPUT_CSV"

echo "Unique positions counted and saved to $OUTPUT_CSV"