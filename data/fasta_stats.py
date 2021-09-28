#!/usr/bin/env python

import sys
import re
import io

if len(sys.argv) != 2:
	print("Usage: fasta_dna_stats <fasta_file>")
	print("This script is for informational purposes only, and requires that the input file be a DNA (As, Ts, Cs, and Gs) FASTA-formatted file.")
	quit()


####### Parse input
def fasta_hash_from_file(filename):
	handle = io.open(filename, "r")
	seqs_dict = dict()
	current_id = ""
	current_seq_list = list()
	
	for line in handle:
		line_list = re.split(r"\s+", line.strip())
		if re.match(r"^>", line_list[0]):
			if current_id != "":
				seqs_dict[current_id] = "".join(current_seq_list)
			current_id = re.subn(r"^>", "", line_list[0])[0]
			current_seq_list = list()
		else:
			current_seq_list.append(line_list[0])

	seqs_dict[current_id] = "".join(current_seq_list)
	
	return seqs_dict


def longest_perfect_repeat(seq):
	result = re.finditer(r"(.{1,10}?)\1{1,}", seq)
	max = 1
	maxrep = seq[0]
	maxunit = seq[0]
	for match in result:
		unit = match.group(1)
		if len(match.group(0)) > max and len(set(unit)) > 1:
			max = len(match.group(0))
			maxrep = match.group(0)
			maxunit = match.group(1)

	return [max, maxrep, maxunit]


def gc_content(seq):
	gccount = 0
	## strings are iterable too ;)
	for base in seq:
		if base == "G" or base == "C" or base == "g" or base == "c":
			gccount = gccount + 1
	rounded = int(float(gccount)/len(seq)*1000)/1000.0
	return(rounded)


def most_common_fivemer(seq):
	mers = dict()
	for index in range(0, len(seq) - 5 + 1):
		fivemer = seq[index:index+5]
		if fivemer in mers:
			mers[fivemer] = mers[fivemer] + 1
		else:
			mers[fivemer] = 1

	max = 0
	maxmer = ""
	for fivemer in mers:
		if mers[fivemer] > max:
			max = mers[fivemer]
			maxmer = fivemer

	return [maxmer, max] 


filename = sys.argv[1]
seqs_dict = fasta_hash_from_file(filename)

print("# Column 1: Sequence ID")
print("# Column 2: GC content")
print("# Column 3: Length")
print("# Column 4: Most common 5mer")
print("# Column 5: Count of most common 5mer")
print("# Column 6: Repeat unit of longest simple perfect repeat (2 to 10 chars)")
print("# Column 7: Length of repeat (in characters)")
print("# Column 8: Repeat type (dinucleotide, trinucleotide, etc.)")

types = dict()
types[1] = "uninucleotide"
types[2] = "dinucleotide"
types[3] = "trinucleotide"
types[4] = "tetranucleotide"
types[5] = "pentanucleotide"
types[6] = "hexanucleotide"
types[7] = "heptanucleotide"
types[8] = "octanucleotide"
types[9] = "enneanucleotide"
types[10] = "decanucleotide"

for id in seqs_dict:
	sys.stderr.write("Processing sequence ID " + id + "\n")

	seq = seqs_dict[id]
	sys.stdout.write(id + "\t")
	sys.stdout.write(str(gc_content(seq)) + "\t")
	sys.stdout.write(str(len(seq)) + "\t")

	maxmer = most_common_fivemer(seq)
	sys.stdout.write(maxmer[0] + "\t")
	sys.stdout.write(str(maxmer[1]) + "\t")
	
	longest_rep_list = longest_perfect_repeat(seq)
	sys.stdout.write("unit:" + longest_rep_list[2] + "\t")
	sys.stdout.write(str(longest_rep_list[0]) + "\t")
	sys.stdout.write(types[len(longest_rep_list[2])])

	sys.stdout.write("\n")