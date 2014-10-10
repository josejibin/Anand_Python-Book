def treemap(a,b,):
  l=[]
  
  for each in b:
    if isinstance(each,list):
      l.append(treemap(a,each))
    else:
      l.append(a(each))
  return l
f=treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
print f  
  
