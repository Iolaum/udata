#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Original code taken at 23.2.2016 from:
# http://stackoverflow.com/a/3207973/1904901

from os import listdir
from os.path import isfile, join
from os import walk
import pickle

# Get a list of all files to be processed in each directory!

# Read and Write list to a file in python - taken at 23.2.2016
# http://stackoverflow.com/a/17225333/1904901

listfile = "prp2_dirlist.pickle"


with open(listfile, 'rb') as f:
    my_list = pickle.load(f)
    
print my_list


for il in my_list:
	filelist = []
	for (dirpath, dirnames, filenames) in walk(il):
		filelist.extend(filenames)
		filelist.sort()
		dfile = "prp3_" + dirpath.split("/")[-1] + ".txt"
		break
	for key,value in enumerate(filelist):
		filelist[key] = join(il, value)
	with open(dfile, 'wb') as f:
		pickle.dump(filelist, f)
