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


# Remove all non alphaneumerical characters from string
# http://stackoverflow.com/a/1277047/1904901
# taken at 29.2.2016
pattern = re.compile('[\W_]+')

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
with open('../dataset/words.txt', 'rb') as f:
	NWORDS = train(words(f.read()))


print("Successfuly created Spell Check dictionary")


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
print("Created list of books to perform first spell check.")


namepatt = re.compile('../dataset/Out_prp3_')
namepatt2 = '../dataset/Out_p9a_'
endpatt1 = re.compile('.txt')
endpatt2 = '.p'


bookctr = 1
for book in listbooks:
    with open(book, 'rb') as f:
        lines = f.readlines()


# # dictionary of error words
    erwords = collections.defaultdict(int)
# change to be able to save !
# http://stackoverflow.com/a/16439720


# Show time progress in console!
# http://stackoverflow.com/a/3173338 // taken at 15.3.2016
    fulltime = len(lines)
    ctr = 0

    print("Starting first spell check run on book {}/24...".format(bookctr))

    for line in lines:
        dwords = line.rstrip('\n').split()
        for dword in dwords:
            # remove non alphaneumerical characters
            dword = pattern.sub('', dword).strip()
            # spell check if appropriate
            if len(dword) > 0 and (not dword.isdigit()):
                cword = correct(dword)
            if cword is not dword:
                erwords[dword] += 1
        # prints percentage of loop progress on console
        ctr += 100
        per = ctr/fulltime
        sys.stdout.write("\r%d%%" % per)
        sys.stdout.flush()
        # break

    terr = 0
    nerr = 0
    for key in erwords:
        terr += erwords[key]
        if erwords[key] > 4:
            nerr += 1

    print("\nTotal Number of True  Errors found on book {}/24: {}.".format(bookctr, terr))
    print("Total Number of False Errors found on book {}/24: {}".format(bookctr, nerr))

    book = namepatt.sub(namepatt2, book)
    book = endpatt1.sub(endpatt2, book)
    with open(book, 'wb') as f:
        pickle.dump(erwords, f)

    bne = len(book) - 2
    print("Book {} Successfully processed!".format(book[18:bne]))
    bookctr += 1

