def val(d):
  l=[]
  r=[]
  for wo,co in d.items():
    l.append((wo,co))
  l.sort()
  for each in l:
    r.append(each[1])
  print r
val({'f':5,'w':7,'a':6})  
