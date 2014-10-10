def cusum(l):
  n=0
  s=[]
  for each in l:
    n+=each
    s.append(n)
  return s
print cusum([4,6,3,8])
