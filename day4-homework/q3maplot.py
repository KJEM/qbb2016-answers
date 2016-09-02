#!/usr/bin/env python

import sys
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
#import re

"""
Instead of plotting FPKM values for SRR072893 and SRR072915 directly, 
transform the data to make an MA-plot. 
This time do not drop rows with 0 FPKM. plt.scale( 'log' ) is not enough 
so you will have to log etc your values first.
Use:
./q3maplot.py ~/data/results/stringtie/SRR072893/t_data.ctab ~/data/results/stringtie/SRR072915/t_data.ctab
"""

srr_893 =sys.argv[1] 
srr_915 =sys.argv[2] 

ctab1_data= pd.read_csv(srr_893,sep="\t")
ctab2_data= pd.read_csv(srr_915,sep="\t")
# print(ctab_data)
FPKM1_data = np.log2(ctab1_data["FPKM"] +1).tolist()
FPKM2_data = np.log2(ctab2_data["FPKM"] +1).tolist()
# print(FPKM1_data)
MA_data_M=[]
MA_data_A=[]
# print(FPKM1_data)

for i,out in enumerate(FPKM1_data):
	# print(FPKM2_data[i])
	MA_data_M.append(FPKM1_data[i]-FPKM2_data[i])

for j,out in enumerate(FPKM1_data):
	MA_data_A.append(0.5*(FPKM1_data[j]+FPKM2_data[j])) 

# print(MA_data_Y)
# print(ctab_data[filter_FPKM])
plt.figure()
plt.title("MA plot for FPKM")

plt.scatter( x=MA_data_A, y=MA_data_M, alpha=0.2)
plt.ylabel("M (log2(SRR072893)-log2(SRR072915))")            # Label the y-axis
plt.xlabel("A (1/2 (log2(SRR072893)-log2(SRR072915))")  
plt.show()
plt.savefig("q3maplot.png")
plt.close()