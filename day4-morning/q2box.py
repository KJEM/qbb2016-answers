#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
""""
./q2box.py <windowsize> <sample1> <sample2> ... 
~/data/results/stringtie/SRR072915/t_data.ct
"""
sample = len( sys.argv[0:])

for i in range(2, sample):
  
    df = pd.read_table( sys.argv[i] ) 
    srr = sys.argv[i].split("/")[-2]
    chroList = []
    #print srr
    
    #filter for Sxl and FPKM
    chroList = ["2L", "2R", "3L", "3R", "4", "X"]
    print len(chroList)
    for j in chroList:
        chX = df["chr"] == j
        chX = df[chX]
        smoothed = chX[ "FPKM" ].rolling( int( sys.argv[1] ) ).mean()


        plt.figure()
        plt.plot( smoothed )
        plt.title( "Rolling mean (size = {}) Chromosome {}".format(sys.argv[1], j))
        plt.xlabel(" Relative position of Chromosome (line number) ")
        plt.savefig( "Rolling mean (size = {}) Chromosome {}.png".format(sys.argv[1], j) )
        plt.close()    
     

#end loop BEGIN PLOT