def peep(q):
  a=q
  b=a
  for each in a:
    
    yield b[0],b
    b=b[1:]
def call(q):
  return q
q=peep(range(5))
e=call(q)
for each,one in e:
  print each,one
  

