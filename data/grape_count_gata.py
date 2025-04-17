#!/usr/bin/env python
import re

def count_motifs(seq, motif):
    pieces = re.split(motif, seq)
    return len(pieces) - 1

with open("grape_promoters.txt", "r") as fhandle:
    for line in fhandle:
        linestripped = line.strip()
        line_list = re.split(r"\s+", linestripped)
        gid = line_list[0]
        seq = line_list[1]


        num_motifs = count_motifs(seq, r"[AT]GATA[GA]")
        print(f"{gid}\t{num_motifs}")