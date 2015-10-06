#!/usr/bin/python

import sys
import urllib2
from os import system
import time, threading

def check_url(url):
    try:
        response = urllib2.urlopen(url)
        system('say site is up!')
    except:
        print url, 'still down:', time.ctime()

def repeat():
    check_url(url)
    threading.Timer(60, repeat).start()

if len(sys.argv) > 1:
    url = sys.argv[1]
else: 
    url = raw_input('URL to check: ')

repeat()