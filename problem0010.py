# projecteuler.net solutions
def solution0010(n = 2000000):
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