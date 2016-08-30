#!/usr/bin/env python

import sys
f = open ( "/Users/cmdb/data/893.sam" )
count = 0
total = 0

for line in f:
    if line.startswith( "SRR" ): 
        val = int(line.split("\t")[4] ) 
        if val == 255:
            continue
        total = total + val    
        count = count + 1    
Avg = total/float(count)        

print Avg
        
        