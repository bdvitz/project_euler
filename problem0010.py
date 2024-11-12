# projecteuler.net solutions
def solution0010(n = 2000000) -> int:
    """ Return the sum of prime numbers below n using sieve of erotosthenes """
    assert n > 1, 'must be larger than one'
    
    # initialize a list to mark all primes
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False # 0 and 1 are not primes
    
    # implement the sieve of erotosthenes, tracking the sum of primes up to sqrt(n)
    prime_sum = 0
    for start in range(2, int(n**0.5)+1):
        if is_prime[start]:
            # loop through all necessary cases if start**2 is less than n+1
            for multiple in range(start**2, n+1, start):
                is_prime[multiple] = False
            # sum the primes at the same time
            prime_sum += start
    
    # get the remaining numbers from sqrt(n) to n
    for start in range(start+1, n+1):
        if is_prime[start]:
            prime_sum += start
    
    return prime_sum
    
def solution0010_slow(n = 2000000):
    """ return the sum of prime numbers below n """
    assert n > 0, 'must be larger than zero'
    if n == 1:
        return 2
    
    # define a stream for odd numbers
    def odd_stream(start: int):
        """ returns a stream that yields odd numbers forever
        start: first odd number """
        
        assert start % 2 == 1, 'input must be odd'
        def helper():
            nonlocal start
            while True:
                yield start
                start += 2
        return helper()
    
    # loop through odd numbers until the maximum is reached
    primes = [3]
    gen = odd_stream(5)
    curr = 1
    n-=2
    while curr < n:
        curr = next(gen)
        root = int(curr**0.5) + 1
        for i in range(len(primes)):
            p = primes[i]
            if curr % p == 0 or p >= root:
                break
        if p >= root:
            primes.append(curr)
        # if not any( curr % p == 0 for p in primes if p < root):
        #     primes.append(curr)
        
    return sum(primes)+2
    
if __name__ == "__main__":
    print(solution0010())