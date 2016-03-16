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


import pickle
import glob  # alternative file finder/selector !!
import re       # to remove non alphaneumerical characters from line.
import string   # to remove non alphaneumerical characters from line.
import collections  # for spell checking
import time  # to show loop progress
import sys   # -//-
import os.path  # check if file is there


# Function that checks if book has already been proccessed
def isProsd(filename):
    return os.path.isfile(filename)


# splits string to list of words:
def words(text): return re.findall('[a-z]+', text.lower())


# creates dictionary,
# initializes first value as 1 and adds more for identical words !
def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model


# word list
# https://github.com/dwyl/english-words
with open('../dataset/wordsdict.txt', 'rb') as f:
	NWORDS = train(words(f.read()))


print("Successfuly created Spell Correcting dictionary")


alphabet = 'abcdefghijklmnopqrstuvwxyz'


def edits1(word):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts = [a + c + b for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)


def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)


def known(words): return set(w for w in words if w in NWORDS)


def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)


# Make List of Books
listbooks = []
for name in glob.glob('../dataset/Out_prp3*'):
    listbooks.append(name)
print("Created list of books to perform spell correction.")


# Remove all non alphaneumerical characters from string
# http://stackoverflow.com/a/1277047/1904901
# taken at 29.2.2016
pattern = re.compile('[\W_]+')


namepatt = re.compile('../dataset/Out_prp3_')
namepatt2 = '../dataset/Out_p11_'


bookctr = 1
for book in listbooks:
    fbook = namepatt.sub(namepatt2, book)
    # check if book has already been processed.
    if (isProsd(fbook)):
        print("Book {} has already been processed!".format(fbook[19:]))
        bookctr += 1
        continue
    else:
        print("Book {} has not been processed, starting ...".format(fbook[19:]))

    with open(book, 'rb') as f:
        lines = f.readlines()


# Show time progress in console!
# http://stackoverflow.com/a/3173338 // taken at 15.3.2016
    fulltime = len(lines)
    ctr = 0

    # Open Entry for proccessed book:
    with open(fbook, 'wb') as nf:

        print("Starting spell correct run on book {}/24...".format(bookctr))

        for line in lines:
            dwords = line.rstrip('\n').split()
            for dword in dwords:
                # remove non alphaneumerical characters
                dword = pattern.sub('', dword).strip()
                # spell check if appropriate
                if len(dword) > 2 and (not dword.isdigit()):
                    cword = correct(dword)
                    nf.write(' ' + cword)
            nf.write('\n')

            # prints percentage of loop progress on console
            ctr += 100
            per = ctr/fulltime
            sys.stdout.write("\r%d%% Completed" % per)
            sys.stdout.flush()
            # break

    print("Book {} Successfully processed!".format(fbook[19:]))
    bookctr += 1

