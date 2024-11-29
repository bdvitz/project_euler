# projecteuler.net solutions
def solution0021(threshold: int) -> int:
    """ amicable numbers: return the sum of all amicable numbers under threshold"""
    # function d(n) is defined as the sum of proper divisors of 'n'
    # amicable numbers are such that d(a) == d(b) and a!=b
    
    # solution strategy. Maintain a list of results. if d(a) == b and results[b] == a, then an amicable number is found
    # No need to be careful about double counting amicable numbers because they are paired by definition
    
    def d(n: int) -> int:
        """ Return the sum of proper divisors of 'n' """
        total = 0
        # find possible divisors less than sqrt of input
        for i in range(2, int(n**.5) + 1):
            if n % i == 0:
                total += i + n//i
        return total + 1 # add 1 because divisor 1 was skipped
    
    # initialize the results list
    results = [0] * (threshold+1)
    # initialize variable to track total sum
    total = 0
    # loop through numbers up to threshold, generating results
    for i in range(2, threshold+1):
        results[i] = d(i)
        if results[i] < i and results[results[i]] == i:
            # add amicable numbers to total
            total += i + results[i]
    
    return total
    
if __name__ == "__main__":
    print(solution0021(10000)) # 10000 -> 31626