import os

c=0
global n
n=4
def direc(p,c):
  
  

  print n*' '+os.path.basename(p)
  c=c+4
  global n
  n=0
  s=os.listdir(p)

  for each in s:
    if '.' in each:
 #     print c,each
      print c*' ','|--',each
    else:
  #    print c,each
      print c*' ','|--',
      direc(os.path.abspath(p+'/'+each),c)

direc(os.path.abspath('a'),c)
