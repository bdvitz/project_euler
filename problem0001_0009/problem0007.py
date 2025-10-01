# projecteuler.net solutions
def solution0007_brute_force(n: int):
    """ return the nth prime number"""
    assert n > 0, 'must be larger than zero'
    if n == 1:
        return 2
    
    # define a stream for odd numbers
    def odd_stream(start: int):
        """ yields odd numbers forever """
        assert start % 2 == 1, 'input must be odd'
        def helper():
            nonlocal start
            while True:
                yield start
                start += 2
        return helper()
    
    # loop through odd numbers until the count is reached
    primes = []
    gen = odd_stream(3)
    while len(primes) < n-1:
        curr = next(gen)
        root = int(curr**0.5) + 1
        if not any( curr % p == 0 for p in primes if p < root):
            primes.append(curr)
        
    return primes[-1]
    
if __name__ == "__main__":
    print(solution0007_brute_force(10001))