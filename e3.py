
def e3():
    primes = [ 2 ]
    n = 600851475143
    max_prime = 0
    current_count = 3

    while True:
        is_prime = True
        for p in primes:
            if n % p == 0:
                is_prime = False
                break
            if p * p > n:
                break

        if is_prime:
            primes.append( current_count)
            while n % current_count == 0:
                max_prime = current_count
                n /= current_count

        if n == 1:
            break

        current_count += 1

    return max_prime

if __name__ == '__main__':
    print e3()