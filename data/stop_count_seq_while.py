#!/usr/bin/env python

with open("seq.txt", "r") as fhandle:
    seq = fhandle.readline()
    seq = seq.strip()

    stop_counter = 0
    index = 0
    while index <= len(seq) - 3:
        codon = seq[index:index + 3]
        #print(codon)
        if codon == "TAG" or codon == "TAA" or codon == "TGA":
            stop_counter = stop_counter + 1
        index += 1       # equivalent to index = index + 1

print(stop_counter)