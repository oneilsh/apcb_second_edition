#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Wrong number of parameters."
    echo "Usage: count_ATs.sh <fasta_file>"
    exit
fi

export file=$1

fasta_stats $file | \
    grep 'unit:AT' | \
    grep 'dinucleotide' | \
    wc
