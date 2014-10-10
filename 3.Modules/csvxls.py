import tablib
def ccc(a,b):
  with open(a,'r') as f:
    s=f.read()
  with open(b,'wb') as f:
    f.write(s)
ccc('test.csv','rer.xls')
