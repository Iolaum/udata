#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://baoilleach.blogspot.com/2014/01/convert-distance-matrix-to-2d.html
# Implementing this method - 3.3.2016

import pickle
import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold



# Read Distance Matrix

with open("../dataset/dists.pickle", 'rb') as f:
	dists = pickle.load(f)

# read document names
with open ("../dataset/BoWsListNames.pickle", 'rb') as f:
	names = pickle.load(f)
# replaced with range(24) for better displaying options.



mds = manifold.MDS(n_components=2, dissimilarity="precomputed", random_state=8) #2, 8
results = mds.fit(dists)


coords = results.embedding_

plt.subplots_adjust(bottom = 0.1)
plt.scatter(
    coords[:, 0], coords[:, 1], marker = 'o'
    )
for label, x, y in zip(range(24), coords[:, 0], coords[:, 1]):
    plt.annotate(
        label,
        xy = (x, y), xytext = (-20, 20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

plt.show()
