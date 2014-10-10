def chfre(f):
  d={}
  s=open(f).read()
  
  print s
  for each in s:
    for i in each:
      d[i]=d.get(i,0)+1
  return d

d=chfre('chfre.py')
print d

