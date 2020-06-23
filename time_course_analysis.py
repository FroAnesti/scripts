#!/usr/bin/env python
# coding: utf-8

import os
import glob
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# The style of the plot
sns.set(style="darkgrid")

def main():
    # Reading a json file which includes a dictionary with the mapping between 
    # PhysiCell/Boss integer codes and the corresponding string the description
    with open('cell_phases_dict.json') as fh:
        phases_dict = json.load(fh)
        phases_dict = {int(k):v for k,v in phases_dict.items()}
        
    # The following dict is used to group cell phases into three general classes:
    # Alive, Apoptotic (programmed cell death), Necrotic (Non-programed cell death)
    column_mapping = { 'Ki67_positive_premitotic':'Alive', 
                       'Ki67_positive_postmitotic':'Alive',
                       'apoptotic': 'Apoptotic', 
                       'necrotic_lysed': 'Necrotic',
                       'necrotic_swelling': 'Necrotic' 
                     }

    # folder where the outputfiles are stored
    cell_output_dir = "./run0/output/"

    # Just counting the number of files (each one corresponding to a time snapshot)
    num_of_files = len(glob.glob(cell_output_dir +  "*.txt"))

    # Initializing a Pandas Databrafe to store the data
    columns = ['Time', 'Alive', 'Apoptotic', 'Necrotic']
    # array 49x4 tupou int
    data = np.zeros((num_of_files, 4), dtype=int)       # num_of_files = 49
    df_time_course = pd.DataFrame(columns=columns, data=data)

    #print("Reading cell_output files:")
    # Iterating over all cell_output files
    for i,f in enumerate(sorted(glob.glob(cell_output_dir +  "*.txt"))):
        #print("\tProcessing file: %s %s" %(i,f))
        # the filename includes the simulation time so, we extract the current time
        # from the file's name and store it in the created dataframe
        time = int(os.path.basename(f)[6:-4])   # e.g. "./run0/output/cells_00000.txt". os.path.basename(f) = 'cells_00000.txt'
        # print(time)
        df_time_course.iat[i, 0] = time
        # print(df_time_course.iat[i, 0]) 0-1440, step 30
        
        # reading a cell_output file (plain text ; separated columns)
        # any function can be used here, using pandas is just a shortcut
        df = pd.read_csv(f, sep=";")
        # Rename the phases integer codes (0, 1 etc) using the phases_dict as the mapping
        df.replace(to_replace={'phase': phases_dict}, value=None, inplace=True)
        # Count the number of cells in each phase (# of cells in phase = 0 & # of cells in phase = 1 etc)
        counts = df.groupby('phase').ID.count()
        #print(counts)
        # group the previous phases count into the three general classes:
        # Alive, Apoptotic, Necrotic
        for k, v in counts.to_dict().items():
            # print(k,v)
            df_time_course.at[i, column_mapping[k]] += v
            
    # Set time column as the dataframe index
    df_time_course.set_index('Time', inplace=True)

    maxV = df_time_course.max();
    print(maxV)
    minV = df_time_course.min();
    print(minV)

    normalized = (df_time_course - minV)/(maxV - minV);
    print(normalized)

    #print("Creating figure")
    print(df_time_course)
    # Create a figure
    fig, ax = plt.subplots(1, 1, figsize=(6,4), dpi=150)
    # plot Alive vs Time
    ax.plot(df_time_course.index, df_time_course.Alive, 'g', label='alive')
    # plot Necrotic vs Time
    ax.plot(df_time_course.index, df_time_course.Necrotic, 'k', label='necrotic')
    # plot Apoptotic vs Time
    ax.plot(df_time_course.index, df_time_course.Apoptotic, 'r', label='apoptotic')
    # setting axes labels
    ax.set_xlabel('time (min)')
    ax.set_ylabel('Nº of cells')
    # Showing legend
    ax.legend()
    
    # Saving fig
    fig_fname ="cell_vs_time.png"
    fig.tight_layout()
    fig.savefig(fig_fname)
    print("Saving fig as %s" % fig_fname)

    #print("Creating normalized figure")
    # Create a figure
    fig, ax = plt.subplots(1, 1, figsize=(6,4), dpi=150)
    # plot Alive vs Time
    ax.plot(df_time_course.index, normalized.Alive, 'g', label='alive')
    # plot Necrotic vs Time
    ax.plot(df_time_course.index, normalized.Necrotic, 'k', label='necrotic')
    # plot Apoptotic vs Time
    ax.plot(df_time_course.index, normalized.Apoptotic, 'r', label='apoptotic')
    # setting axes labels
    ax.set_xlabel('time (min)')
    ax.set_ylabel('N of cells')
    # Showing legend
    ax.legend()
    plt.ylim([-0.1, 1.1])
    # Saving fig
    fig_fname =("normalized_cell_vs_time.png")
    fig.tight_layout()
    fig.savefig(fig_fname)
    print("Saving normalized fig as %s" % fig_fname)


main()

