#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # #
#
# 
#
# Guide - taken at 16.3.2016:
# http://brandonrose.org/clustering

from __future__ import print_function
import numpy as np
import pandas as pd
import pickle as p
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import os  # for os.path.basename
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.manifold import MDS
from sklearn.metrics.pairwise import cosine_similarity as csim


with open('../dataset/Out_p22_tfidf.p', 'rb') as f:
    nmatrix = p.load(f)

with open("../dataset/BoWsListNames4.p", 'rb') as f:
	names1 = p.load(f)
	
with open('../dataset/Out_p22_tfvect_terms.p', 'rb') as f:
    terms = p.load(f)
    
    
num_clusters = 6
km = KMeans(n_clusters=num_clusters)

km.fit(nmatrix)


clusters = km.labels_.tolist()
# list of numbers representing

#uncomment the below to save your model 
#since I've already run my model I am loading from the pickle

joblib.dump(km,  '../dataset/Out_p24_km.p')
print("Kmeans cluster results saved.")

#km = joblib.load('doc_cluster.pkl')
#clusters = km.labels_.tolist()
# -------------------

# load vocab frame
with open('../dataset/Out_p12_vocab_dataframe.p', 'rb') as f:
	vocab_frame = p.load(f)


# print(vocab_frame.describe)
print("Top grams per cluster:\n")
#print()
#sort cluster centers by proximity to centroid
order_centroids = km.cluster_centers_.argsort()[:, ::-1] 

for i in range(num_clusters):
    print("Cluster %d words:" % i, end='')
    
    for ind in order_centroids[i, :10]: #replace 6 with n words per cluster
        print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
    print(' \n') #add whitespace
    #print() #add whitespace
    
    '''
    print("Cluster %d titles:" % i, end='')
    for title in frame.ix[i]['title'].values.tolist():
        print(' %s,' % title, end='')
    print() #add whitespace
    print() #add whitespace
    '''


# Specifying random_state so the plot is reproducible.
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)

# Compute distance matrix:
distm = 1 - csim(nmatrix)

pos = mds.fit_transform(distm)  # shape (n_components, n_samples)

xs, ys = pos[:, 0], pos[:, 1]

#create data frame that has the result of the MDS plus the cluster numbers and titles
df = pd.DataFrame(dict(x=xs, y=ys, label=clusters, title=names1)) 

#group by cluster
groups = df.groupby('label')

font = {'family' : 'Normal',
        'size'   : 18}

mpl.rc('font', **font)



# set up plot
fig, ax = plt.subplots(figsize=(17, 9)) # set size
ax.margins(0.05) # Optional, just adds 5% padding to the autoscaling

#iterate through groups to layer the plot
#note that I use the cluster_name and cluster_color dicts with the 'name' lookup to return the appropriate color/label
for name, group in groups:
    ax.plot(group.x, group.y, marker='o', linestyle='', ms=12, 

            mec='none') # label=cluster_names[name],              color=cluster_colors[name], 
    ax.set_aspect('auto')
    ax.tick_params(\
        axis= 'x',          # changes apply to the x-axis
        which='both',      # both major and minor ticks are affected
        bottom='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        labelbottom='off')
    ax.tick_params(\
        axis= 'y',         # changes apply to the y-axis
        which='both',      # both major and minor ticks are affected
        left='off',      # ticks along the bottom edge are off
        top='off',         # ticks along the top edge are off
        labelleft='off')
    
ax.legend(numpoints=1)  #show legend with only 1 point

#add label in x,y position with the label as the film title
for i in range(len(df)):
    ax.text(df.ix[i]['x'], df.ix[i]['y'], df.ix[i]['title'], size=14)  

    
    
plt.show() #show the plot

#uncomment the below to save the plot if need be
#plt.savefig('clusters_small_noaxes.png', dpi=200)


'''Top grams per cluster:

results:

Cluster 0 words: samites, carthaginians, gabies, patricians, cannibal, pretor, volsci, etrurian, plebeian, quintus, decemvirs, aphids, military, loft, quintins, romans, etruria, foe, venenous, cafe,

Cluster 1 words: declines, justinian, lib, christianity, constantinople, konstantin, goths, church, gothic, mahomet, saracens, caliphate, arabs, bishop, lombard, procopius, theodosianus, choree, danube, oriental,

Cluster 2 words: peloponnesian, syracusan, hath, lacedaemonian, argive, alcibiades, corinthian, thucydides, heavyarmed, before, nubia, christ, peloponnesus, pericles, demosthenic, syracuse, harbour, nay, shewing, samoa,

Cluster 3 words: fays, lib, bacchus, plink, pol, homers, gaius, theban, metal, site, mary, districts, stadia, copper, olympic, mithridate, hellenic, comp, seq, northern,

Cluster 4 words: jews, joseph, heron, jerusalem, judex, hath, anteater, highpriest, jewish, moses, prophet, david, slew, sect, thee, hebrew, simon, agrapha, high, thereby,

Cluster 5 words: tactus, germany, vitellus, alba, section, piso, druses, history, vitellins, suet, aspen, cohort, subtonics, silenus, corbula, valens, praetorian, appendix, non, gripping,
'''

