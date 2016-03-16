#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # #
#
# Spell Check !
#
# Create List on False Spell Checking Errors
# And add them in Word List !


import pickle
import glob  # alternative file finder/selector !!



# Read List of Initial Spell Errors
listbooks = []
for name in glob.glob('../dataset/Out_p9a*'):
    listbooks.append(name)
print("Created list of files containing spell false spell errors.")


# Create false spell errors set:
noerr = set()

for book in listbooks:
    with open(book, 'rb') as f:
        erdict = pickle.load(f)
    for key,value in erdict.iteritems():
        if value >= 4 and len(key) > 3:
            noerr.add(key + '\n')

print("Proccessed all files.")


with open('../dataset/words2.txt', 'ab') as f:
    for it in noerr:
        f.write(it)
        
print("Created list of false spelling errors.")
