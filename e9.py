
def e9():
    for c in xrange( 5, 1000 ):
        a, b = 1, 1
        while b < c:
            if a**2 + b**2 == c**2 and a+b+c == 1000:
                return a*b*c

            if a < b:
                a += 1
            else:
                a = 1
                b+= 1


if __name__ == '__main__':
    print e9()