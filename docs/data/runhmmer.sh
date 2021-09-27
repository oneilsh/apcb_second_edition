#!/bin/bash

# check number of input parameters:
if [ $# -ne 3 ]; then
	echo "Wrong number of parameters."
	echo "Usage: runhmmer.sh <query_fasta> <db_fasta> <output_names>"
	exit
fi

export query=$1
export db=$2
export output=$3

muscle -in $query -out $query.aln
hmmbuild $query.aln.hmm $query.aln
hmmsearch $query.aln.hmm $db \
	> $output