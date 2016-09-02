#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from scipy.stats import gaussian_kde
import numpy as np

"""
Create a density plot of the FPKM values for SRR072893.
Use
./q4densityplot.py ~/data/results/stringtie/SRR072893/t_data.ctab
"""


SRR_file =sys.argv[1] 

ctab_893= pd.read_csv(SRR_file,sep="\t")

FPKM_data= ctab_893["FPKM"].tolist()

density=gaussian_kde(FPKM_data)
# print(FPKM_data)
# print(ctab_data[filter_FPKM])

#script below from stack overflow
plt.figure()
plt.title("Density of FPKM (SRR072893)")
xs = np.linspace(0,10,100)
density.covariance_factor = lambda : .25
density._compute_covariance()
plt.plot(xs,density(xs))
plt.ylabel("Density")
plt.show()
plt.savefig("q4densityplot.png")
plt.close()

