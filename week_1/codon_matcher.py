#!/usr/bin/env python
      
      
import sys
import re
import fasta

"""" 
translate amino acids back to nucleotides
Wherever there is a gap in the protein alignment, 
insert three gaps in the sequence
"""


#reference of AA -> codon
codon_matcher = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}

dic= {y:x for x,y in codon_matcher.iteritems()}
dic['-'] = '---'
dic["X"] = 'xxx' 

header = ''
sequence = ''

# # aa_alignment = fasta.fasta_parser(aa_file) #why does this line not make the code work?
aa_seq = sys.argv[1]

for line in open(aa_seq):
      line = line.rstrip("\r\n")
      if line [0] == ">":
            header = line
            print header
      else:
            for i in range(0,len(line)):
                  codon = line[i]
                  sequence += dic[codon]
      if sequence != '':
            print sequence
      sequence = ''                        



            

 











