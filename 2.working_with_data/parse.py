def pars(f,s):
  p=[]
  l=-1
  d=open(f).readlines()
  for each in d:
    a=each.split(s)
    l+=1
    p.append([])
    for each in a:
      p[l].append(each)
  print p
pars("a.txt",',')
