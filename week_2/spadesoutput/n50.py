#!/usr/bin/env python


""""
Read sequences from a fasta file, count the number of times each 
k-mer occurs acroos all sequences and print kmers and counts.

usage: 01-kmer-counter.py k < fasta_file
"""

import sys 
import math
import fasta

file = open("contigs.fasta", "r")
string_list = file.read().split(">")
length = []
# for = open("listoflengths", "w")

for i in range(1, len(string_list)):
      length.append(float(string_list[i].split("_")[3]))
      sortedlist = sorted(length)
# print sortedlist
      
# print "halfway point:"
# half = str(sum(length) / float(2))
# print half
# the total length, G is 47823.0
# the halway point is 23911.5
      
counter = 0
for item in sortedlist:
      if counter < 23911.5:
            counter += item
      else:
            print "N50:"
            print item
            break
                  
   
      

