def readfile(f):
  for each in f:
    print 'read1',each
    for i in open(each):
      print 'readfile',i
      yield i
def fil(line):
  print 'fil',line
  return (l for l in line  if len(l)>100)
def printt(line):
  for i in line:
    print 'print',i
a=readfile(['jk.py'])
b=fil(a)
printt(b)


