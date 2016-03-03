#!/usr/bin/env python
# -*- coding: utf-8 -*-


# # # Compare WordSets # # #

from os import listdir
from os.path import isfile, join
from os import walk
import pickle
import glob # alternative file selector
import numpy as np




# Read File names

with open ("BoWsListNames.pickle", 'rb') as f:
	names = pickle.load(f)
# print names


# read word sets
bsetlist = []
with open("BoWsList.pickle", 'rb') as f:
    bsetlist = pickle.load(f)
print("Read Word Sets Successfully!")





# work from there :
# http://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html


# Need condensed distance matrix
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.squareform.html

