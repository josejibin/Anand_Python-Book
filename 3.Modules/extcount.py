import os

def ext(f):
  d={}
  h=os.listdir(f)
  e=[]
  for each in h:
    a=each.split('.')
    e.append(a[1])
  for each in e:
    y=d.get(each,0)
    d[each]=y+1
  for each in d:
    print d[each],each
ext('a')
