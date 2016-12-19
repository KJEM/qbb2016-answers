#!/usr/bin/env python

import h5py
import numpy as np

file = h5py.File("Out.heat")
# print file

file.keys()

#[u'0.counts', u'0.expected', u'0.positions', u'regions']

ctcf_positions = []
for i, line in enumerate(ctcf):
	      # if i == 0:
      #       continue
      # if i != 0:
      #       enrich = np.log10(counts/expected)
      #       print enrich   
    fields = line.rstrip("\n\r").split("\t")
    if fields[0] == "chrX":
        ctcf_positions.append(fields[1])
    else:
        continue

# print ctcf_position

positions = file['0.positions'][...]

print positions

# print enrich
            
# print "done"

