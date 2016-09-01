#!/usr/bin/env python

import sys
import fasta

k = int( sys.argv[1] )
query = open( sys.argv[2])

for ident, sequence in fasta.FASTAReader( open(sys.argv[3]) ):
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
    
for i in range( 0, len( q_seq )-k ):
    kmer = q_seq[i:i+k]
    if kmer in kmer_counts:
        matches = kmer_counts[kmer]
        query_start = i
        target_start = matches
        target_sequence_name = ident
        print target_sequence_name, target_start, query_start, kmer

            
           
        
        

    
                
                
                
                    
        