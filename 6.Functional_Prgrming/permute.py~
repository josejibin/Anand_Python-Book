def permute(a,b):
  x=len(a)
  y=len(b)
 
  if y==2:
    z.append(a[:-2]+[b[0]]+[b[1]])
    z.append(a[:-2]+[b[1]]+[b[0]])
    return

  for i in range(y):
    n=b[1:]
    permute(a,n)
    temp=b[y-i-1]
    b[y-i-1]=b[0]
    b[0]=temp
    a=a[:x-y]+b[:]
z=[]
permute([1,2,3,4,5],[1,2,3,4,5])  
print z
    
