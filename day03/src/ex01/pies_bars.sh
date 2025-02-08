#!/bin/bash

if ! python3 -c "import termgraph" &> /dev/null; then
    pip install termgraph
fi

termgraph data.txt --color {yellow,blue}