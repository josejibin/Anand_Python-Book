def unique(l,v):
  w=[]
  u=[]
  for each in l:
    u.append(v(each))
  for each in u:
    if each not in w:
      w.append(each)
  return w
key=lambda s : s.lower()
print unique(['python','dfg','PYTHON'],key)

