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

class MyHTMLParser(HTMLParser):
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
            text = sub('OCR Output', '', text)
            text = text.lower() # convert to lowercase
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')
        elif tag == 'title':
            return

    def handle_startendtag(self, tag, attrs):
        if tag == 'p':
            self.__text.append('\n\n')
        elif tag == 'br':
            self.__text.append('\n')
        elif tag == 'title':
        	return

    def text(self):
        return ''.join(self.__text).strip()


def dehtml(text):
    parser = MyHTMLParser()
    #  HTMLParser.feed(data): Feed some text to the parser.
    parser.feed(text)
    parser.close()
    return parser.text()

# read list of directrories that represent a book


listbooks = []
for name in glob.glob('prp3_gap*'):
	listbooks.append(name)
print listbooks

fileprefix = "Out_"

# iterate over the books
for il in listbooks:
	listfiles = []
	with open(il, 'r') as fl:
		listfiles = pickle.load(fl)
		
	# iterate over the pages	
	for ip in listfiles:
		with open(ip) as inp :
			tdata = dehtml(inp.read())
		with open(fileprefix + il, "a") as tf:
			tf.write(tdata)
	print("Saved file " + fileprefix + il)

print("Parsing Finished Successfully!")

