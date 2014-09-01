#!/usr/bin/python

import urllib2
import pickle
import pprint

fp = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
fp_list = pickle.load(fp)
fp.close()

pprint.pprint(fp_list)
fp = open('5.txt', 'w')

buf = ""
for list in fp_list:
    for c, n in list: 
        buf += c * n
    buf += '\n'

fp.write(buf)
fp.close()

