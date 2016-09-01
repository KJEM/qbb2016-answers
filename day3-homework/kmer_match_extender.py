#!/usr/bin/env python

import sys
import fasta

k = int( sys.argv[1] )
query = open( sys.argv[2])
target1 = fasta.FASTAReader( open(sys.argv[3]) )
target2 = fasta.FASTAReader( open(sys.argv[3]) )

for ident, sequence in target1:
    sequence = sequence.upper()
    kmer_counts = {}
    matching_kmer = []
     
    for i in range( 0, len( sequence )-k ):
        kmer = sequence[ i : i+k ]
        if kmer not in kmer_counts:
            kmer_counts [kmer] = []
        kmer_counts[ kmer ].append(i)

for q_id, q_seq in fasta.FASTAReader( query ):
    pass
    
print q_id, q_seq[0:5]
    
for j in range( 0, len( q_seq )-k ):
    kmer = q_seq[j:j+k]
    if kmer in kmer_counts:
        matches = kmer_counts[kmer]
        query_position = j
        target_position = matches
        identifier = ident
        #return (identifier, target_position, query_position, kmer)
        #print identifier, target_position, query_position, kmer  
        
        if q_seq[j- 1] == sequence[i- 1]:
            ext_kmer = q_seq[i-1]+kmer
            print ext_kmer
            #loop_condition = True
        
        """while q_seq[j- 1] == sequence[i- 1]:
            ext_kmer = q_seq[i-1]+kmer
            print ext_kmer"""
        # num = range(1, 10)
#         if q_seq[j- num] == sequence[i- num]:
#             ext_kmer = q_seq[i-w]+kmer
#         print ext_kmer
        
        #if q_seq[j-2] == sequence[i-2]:
            
        