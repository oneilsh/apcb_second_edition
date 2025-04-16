#!/usr/bin/env python
import MyVCFModule
import sys

## Check usage syntax, read filename 
if len(sys.argv) != 2:
    print("This program parses a VCF 4.0 file and counts")
    print("transitions and transversions on a per-chromosome basis.")
    print("")
    print("Usage: ./snps_ex2.py <input_vcf_file>")
    quit()

filename = sys.argv[1]

chrnames_to_chrs = MyVCFModule.vcf_to_chrnames_dict(filename)

## Print the results!
print(f"chrom\ttransitions\ttransversions")
for chrname in chrnames_to_chrs:
    chr_obj = chrnames_to_chrs[chrname]
    trs = chr_obj.count_transitions()
    trv = chr_obj.count_transversions()
    print(f"{chrname}\t{trs}\t{trv}")