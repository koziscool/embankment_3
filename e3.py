
def e3():
    primes = [ 2 ]

    def next_prime( primes ):
        test_num = primes[-1] + 1
        while True:
            for p in primes:
                if test_num % p == 0:
                    test_num += 1
                    break
                if p * p > test_num:
                    primes.append( test_num )
                    return test_num

    def lpf( current_answer, last_prime, n, primes ):
        return koz

    n = 13195
    current_answer = 1

    while primes[-1] * primes[-1] < n:
        next_prime( primes )

    while n > 1:
        p = lpf( current_answer, primes[-1], n, primes )
        while n % p == 0:
            n /= p




if __name__ == '__main__':
    print e3()