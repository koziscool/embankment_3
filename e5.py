
from collections import defaultdict

primes = [2, 3, 5, 7, 11, 13, 17, 19]

def e5():
    factors_20 = defaultdict(int)

    for i in xrange( 2, 21 ):
        factors = defaultdict(int)
        q = i
        primes_index = 0
        while q > 1:
            p = primes[ primes_index ] 
            while q % p == 0:
                q /= p 
                factors[p] += 1
            factors_20[p] = max( factors_20[p], factors[p] )
            primes_index += 1
            # print i, q

    prod = 1
    for base, exp in factors_20.iteritems():
        prod *= base ** exp
    return prod

if __name__ == '__main__':
    print e5()

