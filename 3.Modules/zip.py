import zipfile
def zipp(a,l):
  zf=zipfile.ZipFile(a,'w')
  for each in l:
    zf.write(each)
  
zipp('ad.zip',['zipp.pyc','wget.py'])

