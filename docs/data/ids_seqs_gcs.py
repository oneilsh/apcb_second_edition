#!/usr/bin/env python

def base_composition(seq: str, query_base: str) -> int:
    """
    Given a DNA (A,C,T,G) string and a 1-letter base string,
    returns the number of occurances of the base in the sequence.
    """
    base_counter = 0
    seq_len = len(seq)
    
    for index in range(0, seq_len):
        seq_base = seq[index]
        if seq_base == query_base:
            base_counter = base_counter + 1
            
    return base_counter

def gc_content(seq: str) -> float:
    '''Given a DNA (A,C,T,G) sequence string, returns the GC-content as float'''
    g_cont = base_composition(seq, "G")
    c_cont = base_composition(seq, "C")
    gc = (g_cont + c_cont)/len(seq)
    return gc

## Open file, and loop over lines
with open("ids_seqs.txt", "r") as fhandle:
    for line in fhandle:
        linelist = line.strip().split("\t")
        id = linelist[0]
        sequence = linelist[1]
        seqgc = gc_content(sequence)
        print(f"{id}\t{seqgc}")