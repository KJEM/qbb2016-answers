#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
import re
from scipy.stats import gaussian_kde
import numpy as np

"""
Create a density plot of the FPKM values for SRR072893.
"""

# df1 = pd.read_table( sys.argv[1] )
# fpkm = np.array( df1["FPKM"] ).reshape(-1, 1)
#
# #print fpkm
#
# kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(fpkm)
# kde.score_samples(fpkm)
SRR_file =sys.argv[1] 

ctab_893= pd.read_csv(SRR_file,sep="\t")

FPKM_data= ctab_893["FPKM"].tolist()

density=gaussian_kde(FPKM_data)
# print(MA_data_Y)
# print(ctab_data[filter_FPKM])

#script below from stack overflow
plt.figure()
plt.title("FPKM {} in Density view".format(re.findall("SRR[0-9]*/",SRR_file)))
xs = np.linspace(0,10,100)
density.covariance_factor = lambda : .25
density._compute_covariance()
plt.plot(xs,density(xs))
plt.show()
plt.savefig("task4density.png")
plt.close()

