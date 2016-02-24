#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Original code taken at 23.2.2016 from:
# http://stackoverflow.com/a/3207973/1904901

from os import listdir
from os.path import isfile, join
from os import walk
import pickle




# # Get list of all data directories [dirs]

mypath = "../dataset/gap-html/"
dirs = []
for (dirpath, dirnames, filenames) in walk(mypath):
    dirs.extend(dirnames)
    break
# print dirs

for key,value in enumerate(dirs):
	dirs[key] = join(dirpath, value)
# print dirs

# use maybe for files?
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


# Read and Write list to a file in python - taken at 23.2.2016
# http://stackoverflow.com/a/17225333/1904901

print "Unsorted!"
for il in dirs:
	print il
dirs.sort()


listfile = "prp2_dirlist.pickle"
with open(listfile, 'wb') as f:
    pickle.dump(dirs, f)

with open(listfile, 'rb') as f:
    my_list = pickle.load(f)
    
print "Sorted!"
for il in dirs:
	print il

