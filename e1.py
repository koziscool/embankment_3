

def e1():
    total = 0
    for i in xrange( 1, 1000):
        if i %3 == 0 or i % 5 == 0:
            total += i
    return total

if __name__ == '__main__':
    print e1()
