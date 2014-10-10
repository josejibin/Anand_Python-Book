def f():
    try:
        print "a"
        return
    except:
        print "b"
    else:
        print "c"
    finally:
        print "d"

f()


