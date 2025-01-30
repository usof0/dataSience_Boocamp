#!/bin/sh

INPUT_CSV="../ex01/hh.csv"
OUTPUT_CSV="hh_sorted.csv"

HEADER=$(head -n 1 "$INPUT_CSV")
tail -n +2 "$INPUT_CSV" | sort -t, -k2,2 -k1,1 > sorted_temp.csv

echo "$HEADER" > "$OUTPUT_CSV"
cat sorted_temp.csv >> "$OUTPUT_CSV"

rm sorted_temp.csv

echo "Sorted CSV file saved to $OUTPUT_CSV"