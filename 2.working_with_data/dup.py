def dup(l):
  le=len(l)
  d=[]
  
  for n in l:
    l=l[1:le]
    if n in l:
      if n not in d:
        d.append(n)
  return d
print dup([4,5,4,6,5,4,3])



