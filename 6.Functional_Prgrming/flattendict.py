def flatten(a,re=None):
  if re is None:
    re={}
  for each in a:
    if isinstance(a[each],dict):
      for i in a[each]:
        b[each+'.'+i]=a[each][i]
      flatten(b,re)
    else:
      re[each]=a[each]
  return re
b={}
q=flatten({'a':1,'b':{'x':2,'y':3},'c':4})
print q
