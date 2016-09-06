#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.decomposition import PCA

"""
./regression.py avgsignal_H3K27.tab ~/data/results/stringtie/SRR072893/t_data.ctab
/Users/cmdb/data/results/stringtie/SRR072893

"""

df = pd.read_table(sys.argv[1])
fpkm_1 = pd.read_table(sys.argv[2]) 
#make dictionary
d = {}
signal_list = []
fpkm_list = []

for i in df.itertuples():
    name = i[1]
    signal = i[6]
    d[name] = [signal]
    
for i in fpkm_1.itertuples():
    name = i[6]
    fpkm = i[-1]
    if name in d:
        d[name].append(fpkm)


for key in d.keys():
    signal = d[key][0]
    fpkm = d[key][1]
    signal_list.append(signal)
    fpkm_list.append(fpkm)


model = sm.OLS(signal_list, fpkm_list)
res = model.fit()
print res.summary()
