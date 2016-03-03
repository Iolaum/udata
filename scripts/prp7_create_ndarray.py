#!/usr/bin/env python
# -*- coding: utf-8 -*-


# # # Compare WordSets # # #

from __future__ import division
from os import listdir
from os.path import isfile, join
from os import walk
import pickle
import glob # alternative file selector
import numpy as np




dists = np.zeros((24,24))
# print(dists)
print("Creted a numpy array of {} dimensions with {} elements!".format(dists.shape, dists.size))

# 


def cdist(a,b):
	c = a & b
	#print("Distance calculated at {}".format(d))
	return 10000/len(c)
	


# read word sets
bsetlist = []
with open("BoWsList.pickle", 'rb') as f:
    bsetlist = pickle.load(f)
#print("Read Word Sets Successfully!")

with open ("BoWsListNames.pickle", 'rb') as f:
	names = pickle.load(f)

print("Let's see how many unique words we have in each document:")

for key1,value1 in enumerate(bsetlist):
	print("In document {} we have {} words!".format(names[key1],len(value1)))
	


# Read File names










# work from there :
# http://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html


# Need condensed distance matrix
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.squareform.html

