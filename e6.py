
def e6():
    sum_squares = lambda n: sum( map( lambda x: x*x, xrange(1, n+1)))
    square_sum = lambda n: ( sum( xrange(1, n+1) ) ** 2 )

    return square_sum(100) - sum_squares(100)

if __name__ == '__main__':
    print e6()