#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # #
#
# Tokenize
#
# Guide - taken at 16.3.2016:
# http://brandonrose.org/clustering


import numpy as np
import pandas as pd
import nltk
import re
# import os
# import codecs
# from sklearn import feature_extraction
# import mpld3
import glob  # alternative file finder/selector !!
import sys
import pickle as p


# Make List of Books
listbooks = []
for name in glob.glob('../dataset/Out_p11*'):
    listbooks.append(name)
print("Created list of books to perform tokenization.")

# load nltk's English stopwords as variable called 'stopwords'
stopwords = nltk.corpus.stopwords.words('english')

# load nltk's SnowballStemmer as variabled 'stemmer'
stemmer = nltk.stem.snowball.SnowballStemmer("english")


# # Tokenization:
# http://www.nltk.org/api/nltk.tokenize.html#module-nltk.tokenize
# Info taken at 16.3.2016

#>>> from nltk.tokenize import word_tokenize
#>>> s = '''Good muffins cost $3.88\nin New York.  Please buy me
#... two of them.\n\nThanks.'''
#>>> word_tokenize(s)
#['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York', '.',
#'Please', 'buy', 'me', 'two', 'of', 'them', '.', 'Thanks', '.']


# Define a tokenizer and stemmer which returns the set of stems in the text that it is passed

def tokenize_and_stem(book):
    print("Started Tokenize and Stem on Book {}".format(book[19:]))
    
    with open(book, 'rb') as fb:
        blines = fb.readlines()
    
    fulltime = len(blines)
    ctr = 0
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = []
    for line in blines:
        for word in nltk.tokenize.word_tokenize(line):
            # add words(n) or numbers more than two characters
            if re.search('[a-z]', word) and len(word) > 2:
                tokens.append(stemmer.stem(word))
            elif re.search('[0-9^a-z]', word) and len(word) > 2:
                tokens.append(stemmer.stem(word))
        # prints percentage of loop progress on console
        ctr += 100
        per = ctr/fulltime
        sys.stdout.write("\r%d%% Completed" % per)
        sys.stdout.flush()
    print("Book {} successfully tokenized and stemmed".format(book[19:]))
    return tokens


def tokenize_only(book):
    print("Started Tokenize only on Book {}".format(book[19:]))
    
    with open(book, 'rb') as fb:
        blines = fb.readlines()
    
    fulltime = len(blines)
    ctr = 0
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = []
    for line in blines:
        for word in nltk.tokenize.word_tokenize(line):
            # add words(n) or numbers more than two characters
            if re.search('[a-z]', word) and len(word)>2:
                tokens.append(word)
            elif re.search('[0-9^a-z]', word) and len(word)>2:
                tokens.append(word)
        # prints percentage of loop progress on console
        ctr += 100
        per = ctr/fulltime
        sys.stdout.write("\r%d%% Completed" % per)
        sys.stdout.flush()  
    print("Book {} successfully tokenized.".format(book[19:])) 
    return tokens



# Create Vocabulary of stemmed words:

#not super pythonic, no, not at all.
#use extend so it's a big flat list of vocab
totalvocab_stemmed = []
totalvocab_tokenized = []
for i in listbooks:
    allwords_stemmed = tokenize_and_stem(i) #for each item in 'books', tokenize/stem
    totalvocab_stemmed.extend(allwords_stemmed) #extend the 'totalvocab_stemmed' list
    
    allwords_tokenized = tokenize_only(i)
    totalvocab_tokenized.extend(allwords_tokenized)
    
    

vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
print('There are ' + str(vocab_frame.shape) + ' items and entries in vocab_frame')

with open('../dataset/Out_p12_vocab_dataframe.p', 'wb') as f:
	p.dump(vocab_frame,f)

print("Vocabulary Dataframe saved!")
