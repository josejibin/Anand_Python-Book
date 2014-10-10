x = 1
def f():
        y = x
        x = 2
        return x + y
print x
# o/p:1
print f()
#UnboundLocalError: local variable 'x' referenced before assignment
print x
#o/p:1

