class yrange:
    def __init__(self, n):
        print 'init'
        self.i = n
        self.n = 0

    def __iter__(self):
        print 'iter'
        return self

    def next(self):
        print 'next'
        if self.i > self.n:
            i = self.i
            self.i += 1
            print i
            return i
        else:
            raise StopIteration()
a=yrange(2)
print 'range'
print list(a)
