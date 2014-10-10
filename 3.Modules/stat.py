import os
p=os.listdir('kk')
r= os.path.abspath('kk')

for each in p:
  s=os.stat(r+'/'+each)  
  print each,' ',s.st_size,' ',s.st_mtime
