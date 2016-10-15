



def is_palindrome( n ):
    if n == int( str( n )[::-1] ):
        return True
    else:
        return False

def e4():
    max_pal = 1
    for i in xrange( 100, 1000 ):
        for j in xrange( i, 1000 ):
            if is_palindrome( i*j ) and i*j > max_pal:
                max_pal = i*j
    return max_pal


if __name__ == '__main__':
    print e4()