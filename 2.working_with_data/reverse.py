def reverse(l):
  le=len(l)
  le-=1
  n=[]
  for  each in l:
    
    n.append(l[le])
    le-=1  
  return n
a=reverse(reverse([1,2,3,4]))
print a    
