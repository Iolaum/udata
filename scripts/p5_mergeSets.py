#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Original code taken at 23.2.2016 from:
# http://stackoverflow.com/a/3207973/1904901


# # # Create List of WordSets # # #

from os import listdir
from os.path import isfile, join
from os import walk
import pickle
import glob # alternative file selector

# Get a list of all files to be processed in each directory!

listbooks = []
for name in glob.glob('Set_Out_prp3*'):
	listbooks.append(name)
# print listbooks

with open("BoWsListNames.pickle", 'wb') as f:
	pickle.dump(listbooks, f)
print("Saved Book List!")

bsetlist = []

for book in listbooks:
	with open(book, 'rb') as f:
		my_list1 = pickle.load(f)
		bsetlist.append(my_list1)
    
print("Created {0} word sets.".format(len(bsetlist)))

with open("BoWsList.pickle", 'wb') as f:
	pickle.dump(bsetlist, f)
		
print("Save Success!")


