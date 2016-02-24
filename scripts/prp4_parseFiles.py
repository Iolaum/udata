#!/usr/bin/env python
# -*- coding: utf-8 -*-

# # #
#
# Read the files in dirs and create a single text file (...)
#
# # # 


# Original _DeHTMLParser code taken [23.2.2016] from:
# http://stackoverflow.com/a/3987802/1904901
# HTMLParser documentation:
# https://docs.python.org/2/library/htmlparser.html

from HTMLParser import HTMLParser
from re import sub # re = regular expression
from sys import stderr
from traceback import print_exc
import pickle
import glob # alternative file selector !!

class _DeHTMLParser(HTMLParser):
	# http://stackoverflow.com/a/17260649/1904901
	# OOP constructs ...
    def __init__(self):
    # Pseudo init function that initializes that HTMLParsers __init__ function as it's __init__ function !!
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
        # re.sub(pattern, repl, string, count=0, flags=0) ... ?
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')

    def handle_startendtag(self, tag, attrs):
        if tag == 'br':
            self.__text.append('\n\n')

    def text(self):
        return ''.join(self.__text).strip()


def dehtml(text):
    parser = _DeHTMLParser()
    #  HTMLParser.feed(data): Feed some text to the parser.
    parser.feed(text)
    parser.close()
    return parser.text()

# read list of directrories that represent a book


listbooks = []
for name in glob.glob('prp3_gap*'):
	listbooks.append(name)
print listbooks


# iterate over the books
for il in listbooks:
	listfiles = []
	with open(il, 'r') as fl:
		listfiles = pickle.load(fl)
		
	# iterate over the pages
	breakcounter = 0
	
	for ip in listfiles:
		breakcounter += 1
	
		if breakcounter > 13:
			break
		with open(ip) as inp :
			tdata = dehtml(inp.read())
		with open("Out" + il, "a") as tf:
			tf.write(tdata)
	break

# it works need fix OCR Output title

