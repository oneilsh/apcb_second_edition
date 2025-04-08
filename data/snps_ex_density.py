#!/usr/bin/env python
## Imports we are likely to need:
import sys
import re

## A class representing simple SNPs
class SNP:
    def __init__(self, chrname, pos, snpid, refallele, altallele):
        assert refallele != altallele, f"Error: ref == alt at pos {pos}"
        self.chrname = chrname
        self.pos = pos
        self.snpid = snpid
        self.refallele = refallele
        self.altallele = altallele

    def is_transition(self):
        '''Returns True if refallele/altallele is A/G, G/A, C/T, or T/C'''
        if self.refallele == "G" or self.refallele == "A":
            if self.altallele == "G" or self.altallele == "A":
                return True

        if self.refallele == "C" or self.refallele == "T":
            if self.altallele == "C" or self.altallele == "T":
                return True

        return False

    def is_transversion(self):
        '''Returns True if the snp is a transversion (i.e., not a transition)
        False otherwise'''
        if self.is_transition():
            return False
        return True
    
## transition test; should not result in "Failed Test"
snp1 = SNP("1", 12351, "rs11345", "C", "T")
assert snp1.is_transition() == True, "Failed Test"      ## Does not error

## transversion test; should not result in "Failed Test"
snp2 = SNP("1", 36642, "rs22541", "A", "T")
assert snp2.is_transversion() == True, "Failed Test"    ## Does not error

## error test; should result in "Error: ref == alt at position 69835"
try:
    SNP("1", 69835, "rs53461", "A", "A")    ## Correctly results in error
    raise Exception("WARNING! Fails to fail when reference matches")
except Exception as e:
    # print(f"Exception:\t{type(e).__name__}")
    # print(f"Description:\t{e}")
    pass        ## catches error in try statement, continues execution


## A class representing a chromosome, which has a collection of SNPs
class Chromosome:
    def __init__(self, chrname):
        self.chrname = chrname
        self.locations_to_snps = dict()

    def get_name(self):
        '''Returns the chromosome name'''
        return self.chrname

    def add_snp(self, chrname, pos, snpid, refallele, altallele):
        '''Given all necessary information to add a new SNP, create a new SNP object 
        and add it to the SNPs dictionary. If a SNP already exists at that location, or
        the given chrname doesn't match self.chrname, an error is reported.'''
        ## If there is already an entry for that SNP, throw an error
        open_location = not(pos in self.locations_to_snps)
        assert open_location, f"Duplicate SNP: {self.chrname}:{pos}"
        
        ## If the chrname doesn't match self.chrname, throw an error
        assert chrname == self.chrname, "Chr name mismatch!"

        ## Otherwise, create the SNP object and add it to the dictionary
        newsnp = SNP(chrname, pos, snpid, refallele, altallele)
        self.locations_to_snps[pos] = newsnp

    def count_transitions(self):
        '''Returns the number of transition SNPs stored in the chromosome'''
        count = 0
        for location in self.locations_to_snps:
            snp = self.locations_to_snps[location]
            if snp.is_transition():
                count += 1
        return count

    def count_transversions(self):
        '''Returns the number of transversion SNPs stored in this chromosome'''
        total_snps = len(self.locations_to_snps)
        return total_snps - self.count_transitions()
    
    def density_region(self, l, m):
        '''returns the number of snps between l and m, divided by the size of the region'''
        count = 0
        for location in self.locations_to_snps:
            if location >= l and location <= m:
                count += 1
        size = m - l  + 1
        return 1000*count/size
    
    def get_last_snp_position(self):
        '''returns the position of the last SNP known'''
        locations = list(self.locations_to_snps.keys())
        locations.sort()
        return locations[len(locations) - 1]

    def max_density(self, region_size):
        '''Given a region size, looks at non-overlapping windows
        of that size and returns a list of three elements for
        the region with the highest density:
        [density of region, start of region, end of region]'''
        region_start = 1
        ## default answer if no SNPs exist [density, start, end]:
        best_answer = [0.0, 1, region_size - 1]

        ## todo: implement this method
        last_snp_position = self.get_last_snp_position()
        while region_start < last_snp_position:
            region_end = region_start + region_size - 1
            region_density = self.density_region(region_start, region_end)
            # if this region has a higher density than any we've seen so far:
            if region_density > best_answer[0]:
                best_answer = [region_density, region_start, region_end]
            region_start = region_start + region_size

        return best_answer

## A test chromosome
chr1 = Chromosome("testChr")
chr1.add_snp("testChr", 24524, "rs15926", "G", "T")
chr1.add_snp("testChr", 62464, "rs61532", "C", "T")

## These should not fail:
assert chr1.count_transitions() == 1, "Failed Test"
assert chr1.count_transversions() == 1, "Failed Test"

## This should fail with a "Duplicate SNP" error:
try:
    chr1.add_snp("testChr", 24524, "rs88664", "A", "C")    ## Correctly results in error
    raise Exception("WARNING! Fails to fail duplicate SNP")
except Exception as e:
    # print(f"Exception:\t{type(e).__name__}")
    # print(f"Description:\t{e}")
    pass        ## catches error in try statement, continues execution

## Check usage syntax, read filename 
if len(sys.argv) != 2:
    print("This program parses a VCF 4.0 file and counts")
    print("transitions and transversions on a per-chromosome basis.")
    print("")
    print("Usage: ./snps_ex.py <input_vcf_file>")
    quit()

filename = sys.argv[1]

## Create chrnames_to_chrs dictionary, parse the input file
chrnames_to_chrs = dict()
with open(filename, "r") as fhandle:
    for line in fhandle:
        # don't attempt to parse header lines (^# matches # at start of string)
        if line[0] != "#":
            line_stripped = line.strip()
            line_list = re.split(r"\s+", line_stripped)

            chrname = line_list[0]
            pos = int(line_list[1])
            snpid = line_list[2]
            refallele = line_list[3]
            altallele = line_list[4]

            ## Put the data in the dictionary
            if chrname in chrnames_to_chrs:
                chr_obj = chrnames_to_chrs[chrname]
                chr_obj.add_snp(chrname, pos, snpid, refallele, altallele)
            else:
                chr_obj = Chromosome(chrname)
                chr_obj.add_snp(chrname, pos, snpid, refallele, altallele)
                chrnames_to_chrs[chrname] = chr_obj

## Print the results!
print(f"chrom\ttransitions\ttransversions\tdensity\tregion")
for chrname in chrnames_to_chrs:
    chr_obj = chrnames_to_chrs[chrname]
    trs = chr_obj.count_transitions()
    trv = chr_obj.count_transversions()

    max_dens_list = chr_obj.max_density(100000)
    density = max_dens_list[0]
    region_start = max_dens_list[1]
    region_end = max_dens_list[2]
    print(f"{chrname}\t{trs}\t{trv}\t{density}\t{region_start}..{region_end}")