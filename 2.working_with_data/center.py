def centre(f):
  r=open(f)
  w=open("new.txt",'w')
  r=r.readlines()
  for each in r:
    w.write("   \t%s"%each)
  w.close() 
centre("she.txt")  
