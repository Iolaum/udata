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


set1 = set()
set2 = set()

set1.add("aa")
set1.add("ab")
set1.add("ac")
set1.add("ad")
set2.add("ab")
set2.add("ac")
set2.add("ad")

def cdist(a,b):
	c = a & b
	d = 10000/len(c)
	print("Distance calculated at {}".format(d))
	return d
	

	
cdist(set1,set2)



# read word sets
bsetlist = []
with open("BoWsList.pickle", 'rb') as f:
    bsetlist = pickle.load(f)
print("Read Word Sets Successfully!")


for key1,value1 in enumerate(bsetlist):
	print key1
	


# Read File names

#with open ("BoWsListNames.pickle", 'rb') as f:
#	names = pickle.load(f)
# print names








# work from there :
# http://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html


# Need condensed distance matrix
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.squareform.html

