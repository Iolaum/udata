#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # #
#
#
#
# Guide - taken at 16.3.2016:
# http://brandonrose.org/clustering


import numpy as np
import pandas as pd
import pickle as p
from sklearn.metrics.pairwise import cosine_similarity as csim
from scipy.cluster.hierarchy import ward, dendrogram
import matplotlib.pyplot as plt
import glob

listbooks = []
for name in glob.glob('../dataset/Out_p11*'):
    print name
    
    
    
""" 
result:
ogsNAAAAIAAJ.txt The Works of Josephus
dIkBAAAAQAAJ.txt The History of Rome - B (Mommsen)
GIt0HMhqjRgC.txt Gibbon's History of the Decline and Fall of the Roman Empire - A
DqQNAAAAYAAJ.txt Livy Vol. 6
Bdw_AAAAYAAJ.txt The History of Rome - A (Livius !!)
udEIAAAAQAAJ.txt Pliny's Natural History, 1, 33
m_6B1DkImIoC.txt Titus Livius Roman History
XmqHlMECi6kC.txt The History Decline and Fall Roman Empire
CSEUAAAAYAAJ.txt The History of the Decline and Fall of the Roman Empire - B
2X5KAAAAYAAJ.txt The Works of Cornelius Tacitus with an Essay on his Life and Genius - A
RqMNAAAAYAAJ.txt Livy Vol. 5
y-AvAAAAYAAJ.txt The Works of Flavuis Josephus, Vol 3
TgpMAAAAYAAJ.txt Flavius Josephus Jewish Antiquities
fnAMAAAAYAAJ.txt The History of the Peloponnesian War by Thoucidides Vol.1
VPENAAAAQAAJ.txt The History and the Fall of the Roman Empire
MEoWAAAAYAAJ.txt The Historical Annals of Cornelius Tacitus
IlUMAQAAMAAJ.txt Gibbon's History of the Decline and Fall of the Roman Empire - B
WORMAAAAYAAJ.txt The Histories of Caius Cornelius Tacitus
CnnUAAAAMAAJ.txt The Whole Genuine Work of Flavius Josephus
aLcWAAAAQAAJ.txt The History of the Decline and Fall of the Roman Empire - A
9ksIAAAAQAAJ.txt The Histrory of the Peloponnesian War
pX5KAAAAYAAJ.txt The Works of Cornelius Tacitus with an Essay on his Life and Genius - B
DhULAAAAYAAJ.txt The Description of Greece
-C0BAAAAQAAJ.txt Dictionary Greek and Roman Geography

"""

names = ['Josephus I', 'Rome - M','Rome V', 'Livy II', 'Livius II', 'Pliny', 'Livius I',
'Rome I','Rome II', 'Tacitus I', 'Livy I', 'Josephus II', 'Josephus III',
'Peloponnesian War I', 'Rome III', 'Tacitus II', 'Rome VI', 'Tacitus III', 'Josephus IV',
'Rome IV', 'Peloponnesian War II', 'Tacitus IV', 'Description Greece', 'Greek Roman G']


for it in names:
    print it
    

with open("../dataset/BoWsListNames4.p", 'wb') as f:
	p.dump(names,f)


