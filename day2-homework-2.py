#!/usr/bin/env python

import sys
import string
f = open ( "/Users/cmdb/qbb2016-answers/day2-homework-1-full.out" )
g = open ( "/Users/cmdb/data/t_data.ctab" )

FlyDic = {}

for line in f:
    field = line.rstrip( "\r\n" ).split( "\t" )
    #field[0] should be... fly_id
    #field[1] should be uniprot id
    FlyDic[field[1]] = field[0] 
    # now we have a dictionay with fly_id : uniprot_id
    
#print FlyDic.keys()
    
for line in g.readlines()[1:]:
    # this skips to the values in the file
    field = line.rstrip( "\r\n" ).split( "\t")
    gene_id = field[8]
    #this is the fly_id   
    if gene_id in FlyDic.keys():
        line = line + "\t" + FlyDic[gene_id]
       
    else:
        line = line + "\t" + "* * *"
    print line
