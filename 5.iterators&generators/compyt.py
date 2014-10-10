import re
import os
def pyt(l):
  n=0
  for each in l:
    
    lis=os.listdir(each)
    for i in lis:
      match=re.search('.py',i)
      if match:
        n += 1
        
      if os.path.isdir(each+'/'+i):
        
        yield each+'/'+i
  print n
def call(a):
  
  return (one for one in a)

l=['a']          
b=pyt(l)

w=call(b)
for each in w:
  l.append(each)

