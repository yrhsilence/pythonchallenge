#!/usr/bin/python
import sys

fp = open('3.txt', 'r')
con = fp.read()

m = {}
for c in con:
    m[c] = m.get(c, 0) + 1

#print [(k, m[k]) for k in sorted(m.keys())]
#print [v for v in sorted(m.values())]
#sort_m1 = sorted(m.iteritems(), cmp = lambda x, y: cmp(x[1], y[1]), reverse = True)
sort_m = sorted(m.iteritems(), key = lambda d: d[1])

result = {}
for i in range(8):
    key = sort_m[i][0]
    result[key] = con.find(key)

sort_r = sorted(result.items(), key = lambda d: d[1])
for item in sort_r:
    sys.stdout.write(item[0])
sys.stdout.write('\n')
