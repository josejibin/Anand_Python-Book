def product(a,b):
  if b==1:
    return a
  else:
    return a+product(a,b-1)
d=product(4,3)
print d
