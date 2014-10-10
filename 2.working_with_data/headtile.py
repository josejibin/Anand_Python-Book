def head(f):
  r=open(f).readlines()
  n=0
  for each in r:
    if n>=10:
      break
    n+=1
    print each
def tile(f):
  r=open(f).readlines()
  e=r[::-1]
  h=e[0:11]
  h=h[::-1]
  print h
  n=0
  for each in h:
    if n>=10:
      break
    n+=1
    print each 
tile('fil.txt')
