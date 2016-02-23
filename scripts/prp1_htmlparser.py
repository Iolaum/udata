#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Original code taken [23.2.2016] from:
# http://stackoverflow.com/a/3987802/1904901
# HTMLParser documentation:
# https://docs.python.org/2/library/htmlparser.html

from HTMLParser import HTMLParser
from re import sub # re = regular expression
from sys import stderr
from traceback import print_exc

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
    try:
        parser = _DeHTMLParser()
        #  HTMLParser.feed(data): Feed some text to the parser.
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        print_exc(file=stderr)
        return text


def main():
    text = r'''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>OCR Output</title>
<meta http-equiv='content-type' content='text/html; charset=utf-8' />
<meta http-equiv='content-style-type' content='text/css' />
<meta name='ocr-capabilities' content='ocr_page ocr_par ocr_cinfo ocr_line' />
<meta name='ocr-system' content='ABBYY fre-8.0.1.1024' />
<meta name='ocr-number-of-pages' content='1' />
</head><body bgcolor='#ffffff'>
<div class='ocr_page'>
<div class='ocrx_block' title='bbox 0 0 1 1'>
<p class='ocr_par' title='bbox 0 0 1 1' style='font-size:0pt;font-family:"Times";font-style:normal'></p>

</div>
</div></body>
</html>'''
    print(dehtml(text))


# http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    main()
