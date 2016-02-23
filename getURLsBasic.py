# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 19:46:06 2016

@author: Malachi
"""

from bs4 import BeautifulSoup
import urllib2
sourceUrl = "http://gd2.mlb.com/components/game/mlb/"
doc1 = urllib2.urlopen(sourceUrl)

soupMaker = BeautifulSoup(doc1, 'html')

urlAppendages = []
for link in soupMaker.find_all('a'):
    urlAppendages.append(link.get('href'))

#grab non-date
'''
for i in range(len(urlAppendages)):
    print sourceUrl+ urlAppendages[i]
'''

