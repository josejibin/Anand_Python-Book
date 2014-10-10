import os
def findfiles(tree):
  
  for one in tree:
    filn=os.listdir(one)
    
    for each in filn:
 
      if os.path.isdir(one+'/'+each):
        
        
        yield one+'/'+each
      else:
        print os.path.abspath(one+'/'+each)
def call(a):

  return (each for each in a)
  
  
l=['a']

a=findfiles(l)
w=call(a)

for each in w:
  
  l.append(each)
  

