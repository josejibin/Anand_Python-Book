def triplets(n):
  l=[]
  [l.append((x,y,z)) for x in range(1,n+1) for y in range(1,n+1) for z in range(1,n+1) if x+y==z]
  b=l
  [b.remove(i) for each in l for i in l if each[0]==i[1] and each[1]==i[0] and each[0] != each[1]]
  #for each in l:
    #print 'each',each
    #for i in l:
   #   print 'i',i
    #  if each[0]==i[1] and each[1]==i[0] and each[0] != each[1]:
   #     b.remove(i)
  return b
print triplets(4)

