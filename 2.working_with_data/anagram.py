def anag(l):
  
  
  le=len(l)
  i=0
  
  n=[]
  m=[]
  d={}
  while le > 0:
    d[i]={}
    for each in l[i]:
      d[i][each]=d[i].get(each,0)+1
    le-=1
    i+=1
  i=0
  le=len(l)
  
  while i<le:
    j=i+1
    n.append([])
    m.append([])
 
    n[i].append(l[i])
    m[i].append(l[i])
    re=len(l)
    while j<re:
 
      if d[i]==d[j]:
       
        m[i].append(l[j])
        n[i].append(l[j])
      j=j+1
    i+=1
  i=0
  y=[]
  le=len(n)
  while i < le:
    j=i+1
    
    while j < le:
      
      if n[j][0] in n[i]:
      
        m[j].append(1)
      j+=1
    i+=1
  
  for each in m:
    if 1 in each:
       m.remove(each)
  print 'm',m 
anag(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
