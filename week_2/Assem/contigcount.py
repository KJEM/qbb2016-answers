#!/usr/bin/env python


""""
Read sequences from a fasta file, count the number of times each 
k-mer occurs acroos all sequences and print kmers and counts.

usage: 01-kmer-counter.py k < fasta_file
"""

import sys 
import math
import fasta

file = open("contigs.fa", "r")
string_list = file.read().split(">")
length = []
# for = open("listoflengths", "w")

for i in range(1, len(string_list)):
      length.append(float(string_list[i].split("_")[3]))
# print length

print "minimum:"
print str(min(length))
print "maximum:"
print str(max(length))
print "average:"
avg = str(sum(length) / float(len(length)))
print avg
#
#
# print "halfway point:"
# half = str(sum(length) / float(2))
# print half

# print length

# sortedlist = sort()
# print sortedlist
#