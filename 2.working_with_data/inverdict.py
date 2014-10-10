def invert(d):
  for wo,nu in d.items():
    del d[wo]
    d[nu]=wo
  print d
invert({'r':4,'t':2,'u':5})
