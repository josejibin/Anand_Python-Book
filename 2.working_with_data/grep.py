def grep(s,f):
  p=open(f).readlines()
  for each in p:
    if s in each:
      print each
grep('seashore','fil.txt')
