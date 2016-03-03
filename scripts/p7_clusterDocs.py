#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pickle
import numpy as np
from scipy.spatial.distance import squareform
import scipy.cluster.hierarchy as hc
import matplotlib.pyplot as plt




# Read Distance Matrix

with open("../dataset/dists.pickle", 'rb') as f:
	dists = pickle.load(f)

# create condensed distance matrix
ndists = squareform(dists)


lnks = hc.linkage(ndists, method='complete')



# Plot dendrogram of hierarchical clustering !
# Works but needs decoration ... 

plt.figure()
hc.dendrogram(lnks)
plt.show()

# work from there :
# http://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html


# Need condensed distance matrix
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.squareform.html

# Additional resources for future reference:
# https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/

