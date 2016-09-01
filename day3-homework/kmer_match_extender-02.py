#!/usr/bin/env python

import sys
import fasta

k = int( sys.argv[1] )
query = open( sys.argv[2])
target1 = fasta.FASTAReader( open(sys.argv[3]) )
target2 = fasta.FASTAReader( open(sys.argv[3]) )
target3 = fasta.FASTAReader( open(sys.argv[3]) )

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
        query_start = i
        target_start = matches
        target_sequence_name = ident
        # print target_sequence_name, target_start, query_start, kmer
        
        
        """if q_seq[j- 1] == sequence[i- 1]:
            ext_kmer = q_seq[i-1]+kmer
            print ext_kmer
            
        if q_seq[j+ 1] == sequence[i+ 1]:
            ext_kmer = kmer+q_seq[i+1]
            print ext_kmer"""
  
        
        for i in range( 0, len( sequence )-k ):
            kmer = sequence[ i : i+k ]
                
        n = 1  
        n += 1+int(len(sequence))
        if q_seq[j- n] == sequence[i- n]:
            ext_kmer = q_seq[i-n]+kmer
            print q_seq[i-n]+kmer
        if IndexError:
            pass
        else:
            q_seq[j- n] != sequence[i- n] 
            pass    
        
        n = 1  
        n += 1+int(len(sequence))
        if q_seq[j+ n] == sequence[i+ n]:
            ext_kmer = q_seq[i-n]+kmer
            print q_seq[i+n]+kmer
        if IndexError:
            pass    
        else:
            q_seq[j- n] != sequence[i+ n] 
            pass
        
            
      
        