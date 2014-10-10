def unique(l,v):
  w=set([])
  u=set([])
  for each in l:
    u.add(v(each))
  for each in u:
    if each not in w:
      w.add(each)
  return w
key=lambda s : s.lower()
print unique({'python','dfg','PYTHON'},key)


