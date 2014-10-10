import sys
def splitt(h,n):
  n=int(n)
  d=open(h).readlines()
  c=len(d)
  
  
  
  j=0
  for each in d:
    if j<n:
      f.write(each)
      j+=1
    else:
      j=0
      yield 
def call(r):
  return (each for each in r)     
r=splitt(sys.argv[1],sys.argv[2])     
a=0
f=open('new'+str(a)+'.txt','wb')
w=call(r)
for each in w:
  a+=1
  f=open('new'+str(a)+'.txt','wb')
