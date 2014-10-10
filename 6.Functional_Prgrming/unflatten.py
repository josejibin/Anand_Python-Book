import re
def unflatten(a,res=None):
  res={}
  for each in a:
    match=re.search('(\w).(\w)',each)
    if match:
      b={}
      for i in a:
        mat=re.search('(\w).(\w)',i)
        if mat:
          if mat.group(1)==match.group(1):
            b[mat.group(2)]=a[i]
      res[match.group(1)]=unflatten(b,res) 
          
       
 
    else:
        res[each]=a[each] 
  return res
  
b={}
f=unflatten({'a':1,'b.x':2,'b.y':3,'c':4})
print f
