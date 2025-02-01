#!/bin/sh

INPUT_CSV="../ex03/hh_positions.csv"

HEADER=$(head -n 1 "$INPUT_CSV")

tail -n +2 "$INPUT_CSV" | while IFS=, read -r id created_at name has_test alternate_url; do
    id=$(echo "$id" | sed 's/"//g')
    created_at=$(echo "$created_at" | sed 's/"//g')
    name=$(echo "$name" | sed 's/"//g')
    has_test=$(echo "$has_test" | sed 's/"//g')
    alternate_url=$(echo "$alternate_url" | sed 's/"//g')
    
    date=$(echo "$created_at" | cut -d'T' -f1)
    if [ ! -f "$date.csv" ]; then
        echo "$HEADER" > "$date.csv"
    fi
  echo "$id,\"$created_at\",\"$name\",$has_test,\"$alternate_url\"" >> "$date.csv"
done

echo "Partitioned CSV files created based on 'created_at' dates."
