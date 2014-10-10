def square(x):
  return x*x
def vector(f):
   n=[]
 
   def h(x):
    
     for each in x:
       n.append(f(each))
     print n
   return h
square=vector(square)
print square
square([1,2,3,4])
