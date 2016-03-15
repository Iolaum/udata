#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # #
#
# Spell Check !
#
# First Simple Implementation!



# Spell Checking taken at 14.3.2016:
# http://norvig.com/spell-correct.html // A
# defaultdict: lamda 1:
# http://stackoverflow.com/questions/8419401/python-defaultdict-and-lambda


# word list taken from  from:
# https://github.com/dwyl/english-words



from re import sub # re = regular expression
import pickle
import glob # alternative file selector !!
import re, string; # to remove non alphaneumerical characters from line.
import pickle
import collections # for spell checking


# Remove all non alphaneumerical characters from string
# http://stackoverflow.com/a/1277047/1904901
# taken at 29.2.2016
pattern = re.compile('[\W_]+')

# Wishful thinking
# run our loops in paraller to take advantage of multi-core!
# http://blog.dominodatalab.com/simple-parallelization/





'''
## 
#
# takes as input the documents Out_prp3*
#
listbooks = []
for name in glob.glob('../dataset/Out_prp3*'):
	listbooks.append(name)
print listbooks



# iterate over the books
for il in listbooks:
	wordslist = []
	with open(il, 'r') as fl:
		for line in fl.readlines():
			words = line.split()
			for word in words:
				# remove non alphaneumerical characters
				word = pattern.sub('', word)
				wordslist.(word)
			#print(line)
			#debug
			#break
	with open("Set_" + il, 'wb') as f:
		pickle.dump(wordslist, f)
	print("Saved wordset Set_" + il)
	# debug
	#break	

print("Wordsets Successfully Created!!")
'''



###
###
###


# splits string to list of words:
def words(text): return re.findall('[a-z]+', text.lower()) 

# creates dictionary, initializes first value as 1 and adds more for identical words !
def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

with open ('../dataset/words.txt', 'rb') as f:
	NWORDS = train(words(f.read()))


print("Read words.txt successfuly!")


alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words): return set(w for w in words if w in NWORDS)

def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)
    
    
###
###
###

print(correct('Thrace'))
# shrape
# Need to take into account names !

# word list
# https://github.com/dwyl/english-words


with open("../dataset/Out_prp3_gap_aLcWAAAAQAAJ.txt", 'rb') as f:
	lines = f.readlines()

ctr=0
for line in lines:
	dwords = line.rstrip('\n').split()
	for dword in dwords:
		# remove non alphaneumerical characters
		dword = pattern.sub('', dword).strip()
		if len(dword) > 0 and ( not dword.isdigit() ) :
			print('Initial word is {}'.format(dword))
			print('Corrected word is {}'.format(correct(dword)))
	ctr += 1
	if ctr == 10:
		break
	


