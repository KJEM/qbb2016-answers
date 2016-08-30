#!/usr/bin/env python

import sys
f = open ( "/Users/cmdb/data/fly.txt" )

new_list=[]
for line in f.readlines():
    if "DROME" in line:
        split_line=line.split()
        if "FBgn" in line:
            new_list.append( (split_line[-2],split_line[-1]) )
        else:
            new_list.append( (split_line[-1], new_list[-1][1]) )
       
for pair in new_list:            
    print pair[0] + "\t" + pair[1]          
        
        
      