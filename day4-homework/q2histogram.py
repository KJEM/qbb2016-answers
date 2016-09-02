#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
Create a histogram of the FPKM values for SRR072893. - filter out 0 values; log the values
./q2histogram.py ~/data/results/stringtie/SRR072893
"""

df = pd.read_table(sys.argv[1])
# hist_roi= hist_data["FPKM"]== "FPKM"
fpkm_1 = df["FPKM"] > 0
filteredfpkm = df[fpkm_1]["FPKM"]
log_fpkm = np.log10(filteredfpkm)

      

# plot

plt.figure()                  # Open blank canvas
plt.hist(log_fpkm)                   # Generate a histogram of the data, with default settings

plt.close()                   # Close the canvas

minimum = np.min(log_fpkm)           # Grab the minimum...
maximum = np.max(log_fpkm)           # ...and maximum value to set the range

plt.figure()                       # Open blank canvas
plt.title("SRR072893") # Add a title to the top
     # Iterate through indices corresponding to the species labels
plt.hist(log_fpkm,                    # ... plot a histogram of
    bins=int(sys.argv[2]),                   # ... ... Use thirty bars
    range=[minimum,maximum],   # ... ... ranging from the minimum to the maximum
    normed=True,               # ... ... Normalize the bars to frequencies instead of counts
    )                          
# plt.legend(loc="upper right")      # Add a legend of with the species labels, to the upper right of the plot.
plt.ylabel("Frequency of FPKM")            # Label the y-axis
# plt.xlabel(labels[0])              # Label the x-axis with the name of the feature we used
plt.savefig("q2histogram.png") 
plt.close()    

   