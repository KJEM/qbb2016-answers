#!/usr/bin/env python

import sys
f = open ( "/Users/cmdb/data/893.sam" )
count = 0
 

for line in f:
    if line.startswith( "SRR" ):
        count = count + 1
        
        
print count    
