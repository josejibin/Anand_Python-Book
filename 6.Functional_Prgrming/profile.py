import time
def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def profile(f):
    def g(x):
        a=time.time()
        value = f(x)
        b=time.time()
        print f.__name__,x,'time:',b-a
        print 'return', repr(value)
        return value
    return g

fib = profile(fib)
print fib
print fib(3)
