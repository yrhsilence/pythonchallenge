#!/usr/bin/python

import re
import urllib2

def get_index(index):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + index 
    html = urllib2.urlopen(url).read()
    print html
    result = re.findall('\d+', html)
    if (len(result) > 0):
        return str(result[-1])
    else:
        return None 

index = '12345'
for i in range(400):
    index = get_index(index)
    if index == None:
        break

index = str(16044 / 2)
for i in range(400):
    index = get_index(index)
    if index == None:
        break
