#!/usr/bin/env python
"""
./q1regions.py ~/data/results/stringtie/SRR072893/t_data.ctab
"""


import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

df = pd.read_table( sys.argv[1] )


lst = []
for i in df.itertuples():
    chromosome = i[2]
    t_name = i[6]
    if chromosome in ("2L", "2R", "3L", "3R", "4", "X", "Y"):
        if i[3] == "+":
            start = int(i[4]) - 500
            end = int(i[4]) + 500
            lst.append((chromosome, start, end, t_name))
        elif i[3] == "-":  
            start = int(i[5]) + 500 
            end = int(i[5]) - 500 
            lst.append((chromosome, start, end, t_name))
    
        
df = pd.DataFrame( lst ) 

df.to_csv( sep="\t" )

print df




# df.to_bed( sys.stdout )
   #  d[ sex + "_" + stage ] = pd.read_table( base
#         + "/results/stringtie" + sample + "/t_data.ctab", index_col="t_name" )
#
#
# #values get assigned right to left
#
# df = pd.DataFrame( d )
# #This is how you make a data frame from a dictionary
#
# df.to_bed( sys.stdout )
#
#

