try:
    print "a"
    raise Exception("doom")
except:
    print "b"
else:
    print "c"
finally:
    print "d"

#o/p
#a
#b
#d

