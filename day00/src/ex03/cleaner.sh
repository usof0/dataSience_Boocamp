#!/bin/sh

INPUT_CSV="../ex02/hh_sorted.csv"

OUTPUT_CSV="hh_positions.csv"

HEADER=$(head -n 1 "$INPUT_CSV")

echo "$HEADER" > "$OUTPUT_CSV"
tail -n +2 "$INPUT_CSV" | while IFS=, read -r id created_at name has_test alternate_url; do
    # Remove quotes
    id=$(echo "$id" | sed 's/"//g')
    created_at=$(echo "$created_at" | sed 's/"//g')
    name=$(echo "$name" | sed 's/"//g')
    has_test=$(echo "$has_test" | sed 's/"//g')
    alternate_url=$(echo "$alternate_url" | sed 's/"//g')

    if echo "$name" | grep -q -E "Junior|Middle|Senior"; then
        new_name=$(echo "$name" | awk '{ for (i=1; i<=NF; i++) if ($i ~ /Junior|Middle|Senior/) print $i }' | tr '\n' '/' | sed 's/\/$//')
    else
        new_name="-"
    fi

    echo "$id,\"$created_at\",\"$new_name\",$has_test,\"$alternate_url\"" >> "$OUTPUT_CSV"
done

echo "Cleaned CSV file saved to $OUTPUT_CSV"