def treerev(a):
  l=[]
  a.reverse()
  for each in a:
    if isinstance(each,list):
      l.append(treerev(each))
    else:
      l.append(each)
  return l

  
k=treerev([[1, 2], [3, [4, 5]], 6])
print k
