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
import pickle as p
from sklearn.decomposition import PCA




with open('../dataset/Out_p18_tfidf_bi.p', 'rb') as f:
	tfidf_matrix = p.load(f)
print('TfIdf matrix type is {}'.format(type(tfidf_matrix)))

tfidf_matrix = tfidf_matrix.toarray()
pca = PCA(n_components=5000)
pca.fit(tfidf_matrix)
nmatrix = pca.transform(tfidf_matrix)

with open('../dataset/Out_p19_svd_bi.p', 'wb') as f:
    p.dump(nmatrix,f)
    
print("Singular Value Decomposition successfully performed !")

