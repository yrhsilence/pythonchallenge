#!/usr/bin/python

#string reverse: s[::-1]

import sys

fp = open('4.txt', 'r')

lines = ""
for line in fp:
    lines += line.strip()

def filte(s):
    return s[1:4].isupper() and s[4].islower() and s[-4:-1].isupper()  \
           and s[0].islower() and s[-1].islower()

for i, _ in enumerate(lines[4:-4]):
    word = lines[i:i+9]
    if filte(word):
        sys.stdout.write(word[4])
sys.stdout.write('\n')
     
    
