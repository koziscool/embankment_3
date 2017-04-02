        
import time

hex_tuples = {}
hex_values = {}
hex_neighbor_dict = {}
hex_neighbor_diffs = {}

hex_plus_one_neighbor_dict = {}
hex_plus_one_neighbor_diffs = {}



def build_primes_up_to(n):
    primes = [2]
    current_counter = 3
    while primes[-1] < n:
        is_prime = True
        for p in primes:
            if p*p > current_counter:
                break
            if current_counter % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append( current_counter )
        current_counter += 1

    primes.pop()
    return primes



three_prime_diff_neighbors = [1, 2, 8]

def build_hex( limit ):
    return map( lambda n: 3*n*n - 3*n + 1, xrange(1, limit + 1))

def build_hex_neighbors( limit_index, hex_nums ):
    primes = build_primes_up_to( 2 * 10 ** 6)

    for i in xrange(2, limit_index-1):
        h = hex_nums[i]

        if ((hex_nums[i] - hex_nums[i-2] - 1) in primes and 
            hex_nums[i] - hex_nums[i-1] - 1 in primes and 
            hex_nums[i+1] - hex_nums[i]- 1 in primes):
            three_prime_diff_neighbors.append( hex_nums[i] )

        plus_one_neighbors = [ hex_nums[i+2], hex_nums[i+1] + 2, hex_nums[i+1] ]
        plus_one_diffs =  [ hex_nums[i+2] - hex_nums[i] - 1, hex_nums[i+1] + 1 - hex_nums[i], hex_nums[i+1] - hex_nums[i] - 1 ]


        if ( hex_nums[i+2] - hex_nums[i] - 1 in primes and 
            hex_nums[i+1] + 1 - hex_nums[i] in primes and 
            hex_nums[i+1] - hex_nums[i] - 1 in primes):
            three_prime_diff_neighbors.append( hex_nums[i] + 1 )

    return hex_nums[i+2] - hex_nums[i] - 1


def e128():
    hex_nums = build_hex( 100005 )
    print build_hex_neighbors( 100000, hex_nums)
    # print plus_one_diffs
    print len(three_prime_diff_neighbors)
    print three_prime_diff_neighbors[9]
    print three_prime_diff_neighbors[-1]
    if len(three_prime_diff_neighbors) >= 2000:
        print three_prime_diff_neighbors[1999]

    # print three_prime_diff_neighbors

 

if __name__ == '__main__':
    start = time.time()
    print
    print "Euler 128 solution is:",  e128()
    end = time.time()
    print "elapsed time is: %.4f milliseconds" % (1000 * (end - start))
