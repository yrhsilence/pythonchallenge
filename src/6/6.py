#!/usr/bin/python

import re
import zipfile

zfp = zipfile.ZipFile("channel.zip")

s_num = 90052
out = ""

num = s_num
while True:
    line = zfp.read('{0}.txt'.format(num))  
    out += zfp.getinfo('{0}.txt'.format(num)).comment.decode()

    try:
        num = re.findall('\d+', line)[-1]
        print line, num
    except Exception, e:
        print e
        print(out)
        break
