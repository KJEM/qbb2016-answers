#!/usr/bin/env python

#Create a boxplot for all the Sxl transcripts that have an FPKM >0 in SRR072893 and SRR072915. log() the values, add a title, label the y-axis, and label each sample on the x-axis.

import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np

numarg = len( sys.argv[1:])

for i in range(1, numarg+1):

    df = pd.read_table( sys.argv[i] ) 
    srr = sys.argv[i].split("/")[-2]    
    
    df_roi = df[ "gene_name" ] == "Sxl"
    df_Sxl = df[ df_roi ]
    df_FPKM = df_Sxl[ "FPKM" ] > 0
    df_exp = df_Sxl[df_FPKM]

 
    fpkm = df_exp[ "FPKM" ]
    #print fpkm
    log_fpkm = np.log10(fpkm)
    
    if i == 1:
        srr_all = [srr]
        logfpkm_all = [log_fpkm]
    else:    
        srr_all.append(srr)
        logfpkm_all.append(log_fpkm)
    
    
#this is the plotting block    
plt.figure()                       # Open a blank canvas
plt.title("Sxl Transcript Expression in FPKM") # Add a title to the top

plt.boxplot(logfpkm_all, labels=srr_all)               # Create a violin plot
#[x[Y==0],x[Y==1],x[Y==2]],     # ...of the values for each species
#labels=species,                # ...with the species names as labels

plt.ylabel("Log 10 FPKM")              # Label the x-axis
plt.xlabel("Samples Across Developmental Timeline")              # Label the y-axis with the first feature name
plt.savefig("clean_boxplot.png")   # Save the plot
plt.close()
