import string
def mutate(s):
  w=[]
  l=len(s)
  old=s
  t=l
  b=l
  let=string.ascii_lowercase
  w.append(s)
  for i in range(0,l):
    
    t=t-1
    new=old[:t]+old[t+1:]
    w.append(new)
    for i in let:
      al=old[:t]+i+old[t+1:]
      r=old[:b]+i+old[b:]
      w.append(al)
      w.append(r)
    b=b-1
  for each in range(l-1):
    sw=old[:each]+old[each+1]+old[each]+old[each+2:]
    w.append(sw)
  
  return w
def nearly(a,b):
  wo=mutate(b)
  return a in wo    


