def group(l,s):
  k=len(l)
  m=[]
  while len(l)>0:
    g=[]
    n=0
    for each in l:
      if n>=s:
        break
      g.append(each)
      n+=1
    m.append(g)
    l=l[s:k]   
  return m
print group([1,2,3,4,5,6,7,8,9],4)
    
