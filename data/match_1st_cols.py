#!/usr/bin/env python
import sys

if sys.stdin.isatty() or len(sys.argv) != 2:
    print("Usage: cat <id_list> | ./match_1st_cols.py <search_file>")
    print("This script extracts lines from <search_file> where any entry")
    print("    in the the first column of <id_list> matches the first column")
    print("    of <search_file>")
    quit()

## Build IDs wanted dictionary from standard input
ids_wanted = dict()
for line in sys.stdin:
    line_stripped = line.strip()
    line_list = line_stripped.split("\t")
    id = line_list[0]
    ids_wanted[id] = "wanted"

## Loop over the file, print the lines that are wanted
with open(sys.argv[1], "r") as fhandle:
    for line in fhandle:
        line_stripped = line.strip()
        line_list = line_stripped.split("\t")
        id = line_list[0]
        # Is the ID one of the ones we want? 
        if id in ids_wanted:
            print(line_stripped)