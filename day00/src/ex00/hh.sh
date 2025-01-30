#!/bin/sh

if [ -z "$1" ]; then
  echo "Usage: $0 <search term>"
  exit 1
fi

SEARCH_TERM=$(echo "$1" | jq -sRr @uri)

curl -s "https://api.hh.ru/vacancies?text=$SEARCH_TERM&per_page=20" | jq '.' > hh.json

echo "Data saved to hh.json"