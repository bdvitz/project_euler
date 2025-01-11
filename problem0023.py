# projecteuler.net solutions
def d(n: int) -> int:
    """ Return the sum of proper divisors of 'n' """
    total = 0
    # find possible divisors less than sqrt of input
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            total += i + n//i
    return total + 1 # add 1 because divisor 1 was skipped

def solution0023(n = 28123) -> int:
    """ Solve problem 23 listed on projecteuler.net
    
    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
    For example, the sum of the proper divisors of 28 would be _, which means that 28 is a perfect number.

    A number is called deficient if the sum of its proper divisors is less than and it is called abundant if this sum exceeds.

    As 12 is the smallest abundant number, _ the smallest number that can be written as the sum of two abundant numbers is.
    By mathematical analysis, it can be shown that all integers greater than 28123 be written as the sum of two abundant numbers.
    However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number
    that cannot be expressed as the sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""
    
    # solution explanation:
    # option 1:
    # (1) find all of the abundant numbers between 24 and 28123-12 to calculate a sum of abundant numbers between 24 and 28123
    # (2) calculate the sum of all positive integers between 24 and 28123
    # (3) calculate the difference (2) minus (1)
    
    # set problem lower bound
    # LOWER_BOUND = 12
    # set problem upper bound
    # UPPER_BOUND = n = 28123
    # generate list of abundants
    abundants = [i for i in range(12,n+1) if isabundant(i)]
    # generate a set of unique values which are the sum of two abundants
    m = len(abundants)
    abundant_sums = set()
    # maintain a total of sums of two abundant numbers
    total = 0
    # nested for loop for O(m^2) runtime
    for i in range(m):
        # threshold to save time on following loop
        threshold = n - abundants[i]
        for j in range(i,m):
            # early exit of current loop
            if abundants[j] > threshold:
                break
            # generate sum of two abundants without (i,j) repeats within 28123 threshold
            curr = abundants[i] + abundants[j]
            if curr not in abundant_sums:
                abundant_sums.add(curr)
                total += curr
    # update to the desired output: the difference between sum(1,2,...,n-1,n) and total
    return (n**2 + n) // 2 - total

def isabundant(num: int) -> bool:
    """ Returns true if a number is abundant, meaning the sum of factors is greater than the number itself """
    total = 0
    # find possible divisors less than or equal to sqrt of input
    for i in range(2, int(num**.5) + 1):
        # check if i is a factor of num
        if num % i == 0:
            # add both factors
            d = num//i # dividend
            total += i + d if (i != d) else i
            # early exit
            if num <= total:
                return True
    # less than or equal to because divisor 1 was skipped
    return num <= total

# from math import factorial
def solution0024(nth_permutation = 1000000, digits = [i for i in range(10)]):
    """ Find the millionth permutation of the numbers 0,1,...,8,9 """
    # Come up with a method of find the nth permutation without listing out the first 1 thru n-1 permutations
    # there definitely already exists a method
    # on method however for a number as small as 10^6 is to try looking only at the last k digits where k! >= 10^6
    
    # bucket, remainder = divmod(10^6,(n-1)!) for n digits to find the bucket of starting digits of the first number
    # Then proceed to iterate until the remainder is gone
    
    # pop the used letter/digit from the list and recursively conduct this process until there is a base case
    
    # can binary search for n given the factorial function and the nth_permutation, but given n = 10 in this case
    # create factorials list where factorials[i] == math.factorial[i+1]
    n = len(digits)
    factorials, prod = [1], 1
    for i in range(1, n):
        prod *= i
        factorials.append(prod)
    
    # reduce the nth_permutation while popping the relevant leading value from the list based on binary search of the factorials list
    # pop factorials from the stack to identify buckets
    p = nth_permutation - 1 # adjust for 0-indexed permutation count - works best for divmod. For instance, the 
    res = [] # results list    
    while factorials and p > 0:
        # generate quotient and remainder for future buckets
        b, p = divmod(p, factorials.pop())
        # if p < curr, then p will not change and b will be zero
        res.append(digits.pop(b))
    
    # return the compiled result list
    return res + digits

# from math import log10
def solution0025(digits = 1000):
    # proposed solution, use modulo 10^7 whenever a number is larger than 10^10
    # make sure to use it for the next two computations
    divisor = 10**7
    threshold = 10**10
    a,b = 1, 1
    index = 2
    limit = 10000
    total_digits = 0
    for index in range(3, limit):
        # increase the fibonacci calculation
        if a > threshold:
            a, b = b // divisor, (a + b) // divisor
            total_digits += 7
        else:
            a, b = b, (a + b)
        
        # check to see if the number of digits matches digits
        if total_digits + log10(b)//1 + 1  == digits:
            return b,index
    
    if index == limit-1:
        return a,b,index

from math import log10
from math import ceil
def solution0026(limit = 1000):
    """ Return d where 1 <= d < limit and the number of repeated digits in 1/d is maximized 
    If there are multiple values of d with the same number of repeated digits, return any of them """
    
    # solution to find the repeated digits
    # 1) compute long form division of the fraction
    # 2) maintain a set of the dividends AFTER correction to a number larger than the divisor
    # d = divisor
    dividend = 1 # first dividend
    vis = dict() # dict for tracking dividends
    
    def increase_dividend(dividend: int, divisor: int) -> int:
        """ Return the minimum value k where dividend * (10**k) >= divisor """
        # k >= log10(d / dividend)
        return ceil(log10(divisor / dividend))
    
    # track the best sequence length found
    best_length = 0
    best_divisor = 0
    # loop through all number 1 thru limit-1
    for divisor in range(1, limit):
        # for each number compute long division until zero or a loop is found
        # initialize variables
        position = 0
        dividend = 1
        vis.clear()
        # loop until complete
        while True:
            # check for non-repeating
            if dividend == 0:
                break
            # continue until duplicate dividend is found
            k = increase_dividend(dividend, divisor)
            position += k
            dividend *= 10**k
            # if not repeated yet
            if dividend not in vis:
                vis[dividend] = position
                dividend = dividend % divisor
            # repetition found
            else:
                # calculate the repeating sequence length
                curr = position - vis[dividend]
                # compare to best sequence length yet and save if better
                if best_length < curr:
                    best_length = curr
                    best_divisor = divisor
                    # print('new best is length:', best_length, ' divisor:', best_divisor)
                # exit the while loop
                break
    return (best_length, best_divisor)

def only_factors_2_and_5(lim = 1000):
    """ Return the list number less than lim that have only 2 and 5 as prime factors """
    s = set()
    for i in range(0,9+1):
        for j in range(0,4+1):
            curr = 2**i * 5**j
            if 1 < curr < lim:
                s.add(curr)
    return(sorted(s))

def solution0027(limit = 1000) -> tuple[int, int]:
    """ Return (a,b) where the number of consecutive primes counted by
    n^2 + an + b starting with n=0 is maximized for abs(a) < limit and abs(b) <= limit """
    
    # # generate primes list, where primes[i] is True if i is prime
    # is_prime = generate_primes(limit**2)
    # primes = set(num for num in len(is_prime) if is_prime[num])
    is_prime = generate_primes(13000)
    
    def count_primes(a: int, b: int) -> int:
        """ Return the number of consecutive primes """
        n = 0
        start = n**2 + a*n + b
        if start < 2: return n
        while is_prime[start]:
            start += 2*n + 1 + a
            n += 1
        return n
    
    best = 40
    best_pair = (1, 41)
    # try inefficient solution
    for a in range(1-limit, limit):
        for b in range(-limit, limit+1):
            curr = count_primes(a, b)
            if best < curr:
                best = curr
                best_pair = (a, b)
    
    return best, best_pair, best_pair[0] * best_pair[1]

# global largest_prime_check
# largest_prime_check = 0
def isprime(num: int) -> bool:
    """ Return true if a number is prime """
    if num < 2: return False
    # global largest_prime_check
    # if largest_prime_check < num: largest_prime_check = num
    for i in range(2, int(num**.5)+1):
        if num % i == 0:
            return False
    return True

def generate_primes(n: int) -> list:
    """ Generate list of primes up to n using sieve of eratosthenes """
    # initialize a list to mark all primes
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False # 0 and 1 are not primes
    
    # implement the sieve of erotosthenes, tracking the sum of primes up to sqrt(n)
    # prime_sum = 0
    for start in range(2, int(n**0.5)+1):
        if is_prime[start]:
            # loop through all necessary cases if start**2 is less than n+1
            for multiple in range(start**2, n+1, start):
                is_prime[multiple] = False
            # sum the primes at the same time
            # prime_sum += start
    return is_prime

def solution0028(n = 1001) -> int:
    """ Return the sum of the diagonals of an n by n
    square matrix formed by starting in the center and spiraling outward
    i.e.
    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13
    """
    # observations:
    # side length must be an odd number
    # each layer after the first has 4 values 
    # The sum of those 4 values is equal to 4 times the left center value
    if n <= 0 or n % 2 == 0:
        return -1
    total = 1
    curr = 1
    for i in range(3, n+1, 2):
        # # Method 1: visual addition of side lengths
        # left1, top, right, bottom, left2 = (i-2)//2, (i-2)-1, i-1, i-1, i//2
        # curr += left1 + top + right + bottom + left2
        
        # method 2: simplified method 1
        curr += 4 * i - 7
        total += 4 * curr
        # print(i, curr, total)
    return total

def solution0029(limit = 100):
    """ Return how many distinct terms there are in the sequence generated
    by a**b for 2 <= a <= limit and 2 <= b <= limit """
    # reduce each 'a' term down to prime factors
    # store prime factors in ordered tuples
    # example 4**6 -> (2, 12) and 6**6 -> (2, 6, 3, 6)
    # maintain a set of these reduced prime factor tuple representation of numbers
    # return the length of the set
    def helper(num: int) -> list[list, list]:
        """ Return a 2d list that contains the prime roots and their powers """
        primes, powers = [], []
        divisor = 2
        while num > 1:
            if num % divisor == 0:
                count = 0
                while num % divisor == 0:
                    num //= divisor
                    count += 1
                # update the primes and powers lists
                primes.append(divisor)
                powers.append(count)
            divisor += 1
        return [primes, powers]
    
    seen = set()
    res = []
    for a in range(2, limit+1):
        # reduce to prime factors
        primes, powers = helper(a)
        # loop through possible powers
        for b in range(2, limit+1):
            res.clear()
            for p, w in zip(primes, powers):
                res.append(p)
                res.append(w * b)
            seen.add(tuple(res))

    return len(seen)

def solve_0023_thru_0029():
    print('solve 23: ', solution0023())
    print('solve 24: ', solution0024())
    print('solve 25: ', solution0025())
    print('solve 26: ', solution0026())
    print('solve 27: ', solution0027())
    print('solve 28: ', solution0028())
    print('solve 29: ', solution0029())
    
if __name__ == "__main__":
    solve_0023_thru_0029()