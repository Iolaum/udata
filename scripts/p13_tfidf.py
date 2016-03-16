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
    with open(name, 'rb') as bf:
        listbooks.append(bf.read())
print("Created list of raw book data to perform tfidf.")

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
    print("Started Tokenize and Stem on Book ??")  # {}".format(book[19:]))

    wbook = book.split()
    del book
    fulltime = len(wbook)
    ctr = 0
    # tokenize
    tokens = []
    for line in wbook:
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
    print("Book ?? successfully tokenized and stemmed")  # .format(book[19:]))
    return tokens


# # Create TfIdfMatrix !
from sklearn.feature_extraction.text import TfidfVectorizer

#define vectorizer parameters
tfidf_vectorizer = TfidfVectorizer(max_df=0.9, max_features=50000,
                                 min_df=0.2, stop_words='english',
                                 use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1, 1))

tfidf_matrix = tfidf_vectorizer.fit_transform(listbooks)  # fit the vectorizer to synopses

print("TfIdf matrix shape: {}".format(tfidf_matrix.shape))

with open('../dataset/Out_p13_tfidf.p', 'wb') as f:
	p.dump(tfidf_matrix, f)

print("TfIdf matrix saved!")

