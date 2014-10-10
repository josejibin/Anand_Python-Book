def extsort(l):
  e=[]
  l.sort(key=lambda s: s.split(".")[1])
  return l           
print extsort(['f.ry','b.py','h.c'])
