def izip(a,b):
  for each in a:
    yield each,b[0]
    b=b[1:]
def call(a):
  return (each for each in a)
q=izip(['a','s','d'],[1,2,3])
e=call(q)
for each,one in e:
  print each,one

