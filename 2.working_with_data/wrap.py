def wrap(f,w):
  d=open(f).readlines()
  for each in d:
    l=len(each)
    if l > w:
      print each[0:w]
      print each[w:l]
    else:
      print each
wrap('fil.txt',30)
