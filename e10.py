
def e10():
    primes = [2]
    current_count = 3

    while primes[-1] < 2 * 10**6:
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

    primes.pop()
    return sum(primes)

if __name__ == '__main__':
    print e10()