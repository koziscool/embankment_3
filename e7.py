
def e7():
    primes = [2]
    current_count = 3

    while len(primes) < 10001:
        is_prime = True
        for p in primes:
            if p**2 > current_count:
                break
            if current_count % p == 0:
                is_prime = False    
                break
        if is_prime:
            primes.append( current_count )

        current_count += 1

    return primes.pop()

if __name__ == '__main__':
    print e7()
