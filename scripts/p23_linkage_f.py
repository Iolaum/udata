#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # #
#
#
#
# Guide - taken at 16.3.2016:
# http://brandonrose.org/clustering


import numpy as np
import pandas as pd
import pickle as p
from sklearn.metrics.pairwise import cosine_similarity as csim
import scipy.cluster.hierarchy as hc
#import ward, dendrogram
import matplotlib.pyplot as plt
import matplotlib


with open('../dataset/Out_p22_tfidf.p', 'rb') as f:
    nmatrix = p.load(f)

with open("../dataset/BoWsListNames4.p", 'rb') as f:
	names1 = p.load(f)

# Compute distance matrix:
distm = 1 - csim(nmatrix)
print("Distance Matrix Computed")

# linkage_matrix = hc.ward(distm)
linkage_matrix = hc.linkage(distm, method='average')
# average ++
#


font = {'family' : 'Helvetical',
        'weight' : 'bold',
        'size'   : 18}

matplotlib.rc('font', **font)

fig, ax = plt.subplots(figsize=(15, 20)) # set size
ax = hc.dendrogram(linkage_matrix, orientation="right", labels=names1, color_threshold=1.33);

plt.tick_params(\
    axis= 'x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='on',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='on')


#plt.tight_layout() #show plot with tight layout
plt.title("Hierarchical Clustering")
plt.show()
plt.close()
