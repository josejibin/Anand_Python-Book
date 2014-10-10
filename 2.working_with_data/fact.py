def product(l):
  n=1
  for each in l:
    n*=each
  return n
def fact(n):
  l=[]
  
  while(n>0):
    
    l.append(n)
    n=n-1
  
  product(l)


