#!/bin/sh

INPUT_CSV="../ex02/hh_sorted.csv"
OUTPUT_CSV="hh_positions.csv"

HEADER=$(head -n 1 "$INPUT_CSV")

echo "$HEADER" > "$OUTPUT_CSV"
tail -n +2 "$INPUT_CSV" | while IFS=, read -r id created_at name has_test alternate_rl; do
    if echo "$name" | grep -q -E "Junior|Middle|Senior"; then
        # new_name=$(echo "$name" | -o -E "Junior|Middle|Senior" | tr '\n' '/' | sed 's/\/$//')
        new_name=$(echo "$name" | awk '{ for (i=1; i<=NF; i++) if ($i ~ /Junior|Middle|Senior/) print $i }' | tr '\n' '/' | sed 's/\/$//')

    else
        new_name="-"
    fi

    echo "$id,\"$created_at\",$new_name\",$has_test\",$alternate_url\"" >> "$OUTPUT_CSV"
done

echo "Cleaned CSV file saved to $OUTPUT_CSV"