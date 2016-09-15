#!/usr/bin/env python

""" 
On the command line, use 

blastn -remote -db nr -query week1_query.fa -outfmt "6 id qstart qend sseq" -evalue 0.0001 > head -1000 blastoutput.tsv

to generate output-- output to blastoutput.tsv


Use this to filter and convert to tsv-- remove dashes and make sure that there are complete sequences
./week1.py ./blastoutput.tsv

blastn -remote -db nr -query week1_query.fa -outfmt "6 id qstart qend sseq" -evalue 0.0001
"""
import sys

f = open(sys.argv[1])

for i, strand in enumerate(f):
      strands = strand.rstrip("\r\n").split("\t")
      roi = strands[2].split("|")
      # print roi
      # nodash = roi.replace("-","")
      # print roi[-1]
      #sequence = roi[-1]
      for j in roi: 
            # if "-" in j:
            nodash = j.replace("-","")
            #       print "true"
            # else:
            #       print
            print nodash
                
                  
#now run in command line and save to a .fa file. 