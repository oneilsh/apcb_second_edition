#!/usr/bin/env python
import sys

if(sys.stdin.isatty()):
    print("Usage: cat <annotation file> | ./go_id_count.py")
    quit()

ids_to_counts = dict()

# Parse input
for line in sys.stdin:
    line_list = line.strip().split("\t")
    seqid = line_list[0]
    if seqid in ids_to_counts:      #seqid already seen, update
        ids_to_counts[seqid] += 1
    else:                           #new seqid, initialize
        ids_to_counts[seqid] = 1

# Print dict contents
for seqid in ids_to_counts:
    count = ids_to_counts[seqid]
    print(count, seqid, sep="\t")