import re  
  
result='1'  
  
pattern=re.compile(r'((?P<w>\d)(?P=w)*)')  
  
for i in range(30):  
    a=map(lambda x:'%s%s'%(len(x[0]),x[1]), pattern.findall(result))  
    result=''.join(a)  
    print a
  
print len(result)  
