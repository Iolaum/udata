#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pickle
import numpy as np
from scipy.spatial.distance import squareform
# Need condensed distance matrix
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.squareform.html
import scipy.cluster.hierarchy as hc
# http://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html
import matplotlib.pyplot as plt



# Read Distance Matrix

with open("../dataset/dists.pickle", 'rb') as f:
	dists = pickle.load(f)

# create condensed distance matrix
ndists = squareform(dists)

lnks = hc.linkage(ndists, method='weighted')


# Plot dendrogram of hierarchical clustering !
# Works but needs decoration ... 


with open("../dataset/BoWsListNames3.pickle", 'rb') as f:
	names1 = pickle.load(f)

plt.figure()
plt.title("Bag of Words Hierarchical Clustering")
hc.dendrogram(lnks, labels=names1, orientation="right", color_threshold=2.17)
plt.tight_layout()

plt.show()



# Additional resources for future reference:
# https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/


