#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Original code taken at 23.2.2016 from:
# http://stackoverflow.com/a/3207973/1904901


# # # Compare WordSets # # #

from os import listdir
from os.path import isfile, join
from os import walk
import pickle
import glob # alternative file selector

# Get a list of all files to be processed in each directory!


bsetlist = []


with open("BoWsList.pickle", 'rb') as f:
    bsetlist = pickle.load(f)

# work from there :
# http://docs.scipy.org/doc/scipy/reference/cluster.hierarchy.html

