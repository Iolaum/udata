#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # #
#
# Create Bag of Words from text file.
#
# First Simple Implementation!



from re import sub # re = regular expression
import pickle
import glob # alternative file selector !!
import re, string; # to remove non alphaneumerical characters from line.
import pickle

# Remove all non alphaneumerical characters from string
# http://stackoverflow.com/a/1277047/1904901
# taken at 29.2.2016

# run our loops in paraller to take advantage of multi-core!
# http://blog.dominodatalab.com/simple-parallelization/



pattern = re.compile('[\W_]+')


listbooks = []
for name in glob.glob('Out_prp3*'):
	listbooks.append(name)
print listbooks



# iterate over the books
for il in listbooks:
	wordset = set()
	with open(il, 'r') as fl:
		for line in fl.readlines():
			words = line.split()
			for word in words:
				# remove non alphaneumerical characters
				word = pattern.sub('', word)
				wordset.add(word)
			#print(line)
			#debug
			#break
	with open("Set_" + il, 'wb') as f:
		pickle.dump(wordset, f)
	print("Saved wordset Set_" + il)
	# debug
	#break	

print("Wordsets Successfully Created!!")

