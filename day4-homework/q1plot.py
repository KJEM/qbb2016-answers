#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt

""" 
Usage: ./q1plot.py <metadata.csv> <ctab_dir> 
    e.g. ./q1plot.py ~/data/fastq/samples.csv ~/data/results/stringtie/ ~/data/fastq/replicates.csv
"""

metadata_dir =sys.argv[1]
ctab_dir = sys.argv[2]
rep_dir = sys.argv[3]

def plot_sex(metadata_dir,ctab_dir,sex):
        metadata= pd.read_csv(metadata_dir)


        metadata_roi= metadata["sex"]==sex
        metadata_result= metadata[metadata_roi]

        FPKM_list=[]
        name_list=[]
        for i,file_dir in enumerate(metadata_result["sample"].tolist()):
                file = open(ctab_dir + file_dir+"/t_data.ctab" )
                sample= pd.read_csv(file,sep="\t")
                filtered_data= sample[sample["gene_name"]=="Sxl"]
                # print(type(filtered_data["FPKM"].values.mean()))
                FPKM_list.append(filtered_data["FPKM"].values.mean())
                name_list.append(metadata_result["stage"].tolist()[i])
                
                #plt.plot(filtered_data["FPKM"].values.mean())#labels=metadata_result["sample"].tolist()[i]
                # plt.plot(range(0,i+1), FPKM_list,'bo-')
        return FPKM_list,name_list

#plot data
fig, ax = plt.subplots()
(FPKM_list,name_list) = plot_sex(metadata_dir,ctab_dir,"female")
plt.plot(range(0,len(FPKM_list)),FPKM_list)
(FPKM_list,name_list) = plot_sex(metadata_dir,ctab_dir,"male")
plt.plot(range(0,len(FPKM_list)),FPKM_list)

#plot replicates
(FPKM_list2,name_list) = plot_sex(rep_dir,ctab_dir,"female")
plt.plot(range (4, len( FPKM_list ) ), FPKM_list2, 'o')
print FPKM_list
(FPKM_list2,name_list) = plot_sex(rep_dir,ctab_dir,"male")
plt.plot(range (4, len( FPKM_list ) ), FPKM_list2, 'o')

plt.title("Sxl")
ax.set_xticklabels(name_list)
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (FPKM)")
plt.savefig("Female_Male_Sxl_FPKM.png")
plt.close()