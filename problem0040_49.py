
def solution0040(power = 7) -> int:
    """ Return the product of dn (i.e. PI [dn]) for n from 10^0 to 10^(power-1) 
    in the irrational decimal fraction that is created by concatenating
    the positive integers
    
    >>> solution0040(2)  # 0.1234567891 has a 1 in both n=1 and n=10 positions. d1 * d10 = 1
    1
    """
    product = 1
    
    # This solution requires an algorithm to efficiently calculate the nth digit
    # simply count the number of digits in the current number range using math
    # the number range increases by 10x every power of 10
    
    def calculateDigit(n: int) -> int:
        """ Returns the nth digit in the sequence """
        position = 1
        power = 0
        # increase the power and position if the current upper bound is less than n
        while True:
            lower, upper = 10**power, 10**(power+1)-1
            
            # determine the number of numbers in the range
            number_count = upper - lower + 1
            
            # determine the number of digits in the range
            digit_count = number_count * (power + 1)
            
            # increase the power
            power += 1
            
            # increase the position if it does not skip past n
            # otherwise, break the loop and find n in the position range
            if n >= position + digit_count:
                position += digit_count
            else:
                break
        
        # now the nth digit falls in the range [position, position + digit_count]
        # the number containing the nth digit and the digit itself
        # can be determined with simple math
        number_index = (n-position) // power
        
        # find the number containing this special digit
        number = lower + number_index
        
        # retrieve the correct digit from the number
        return int(str(number)[(n-position) % power])
    
    # for debugging
    # for i in range(20):
    #     print(calculateDigit(i))
    
    for exponent in range(power):
        ans = calculateDigit(10**exponent)
        product *= ans
        
    return product

from math import isqrt
from math import floor
from math import log10
from itertools import permutations

def solution0041() -> int:
    """ Return the largest pan-digital prime number """
    # check if a number is prime quickly
    # if the sum of 
    
    def is_prime(n):
        """Return True if n is a prime number, else False."""
        # # ignore less than 1 for efficiency
        # if n <= 1:
        #     return False
        if n <= 3:
            return True  # 2 and 3 are prime
        if n % 2 == 0 or n % 3 == 0:
            return False  # eliminate multiples of 2 and 3
        
        # check only numbers of from 6k ± 1 up to sqrt(n)
        limit = int(isqrt(n)) + 1
        for i in range(5, limit, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True
        
    def is_n_digits(n, low, high):
        """ Checks if all digits between 1 and n are used """
        return seen[1] and high - low == floor(log10(n))
    
    seen = [False] * 10
    answer = 1
    
    def check(number: int, low: int, high: int):
        nonlocal answer
        if answer < number and is_n_digits(number, low, high) and is_prime(number):
            answer = number
    
    def backtrack(count: int, curr: int, low=10, high=0):
        if count <= 3:
            # check if the current number is prime and set to the maximum possible prime
            check(curr, low, high)
        
        if count == 0:
            return
        
        for i in range(1,10):
            if not seen[i]:
                seen[i] = True
                backtrack(count-1, curr*10 + i, min(low, i), max(high, i))
                seen[i] = False
    
    backtrack(9, 0)
    return answer

def solution0041_improved() -> int:
    """ Return the largest pan-digital prime number """
    def is_prime(n):
        """Return True if n is a prime number, else False."""
        # # ignore less than 1 for efficiency
        # if n <= 1:
        #     return False
        if n <= 3:
            return True  # 2 and 3 are prime
        if n % 2 == 0 or n % 3 == 0:
            return False  # eliminate multiples of 2 and 3
        
        # check only numbers of from 6k ± 1 up to sqrt(n)
        limit = int(isqrt(n)) + 1
        for i in range(5, limit, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    answer = 2143
    for i in range(1, 10):
        for perm in permutations(range(1,i+1)):
            # check if the current permuatation is a solution
            # convert to a number
            num = 0
            for j in range(i):
                num *= 10
                num += perm[j]
            
            # check if the number is better
            if answer < num and is_prime(num):
                answer = num
    
    return answer

import csv
from wrappers import wraps

def cache(f: callable):
    """ typical caching decorator function for practice """
    results = {}
    @wraps(f)
    def wrapper(*args, **keywords):
        key = (args, tuple(sorted(keywords.items())))
        if key not in results:
            results[key] = f(*args, **keywords)
        return results[key]
    return wrapper
    
def solution0042() -> int:
    """ Return the count of the words in the text file that have values equivalent
    to a triangle number"""
    # fast check for a triangle number is to multiply by two, check the sqrt,
    # then determine the possible n^2 + n value for n as an integer.
    # take the floor, then recalculate (n^2 + n )
    def word_score(word: str):
        score = 0
        for char in word:
            score += ord(char.lower()) - ord('a') + 1
        return score
    
    @cache
    def triangle_number(score: int) -> bool:
        """ Return true if this is a triangle number """
        n = isqrt(score * 2)
        return score * 2 == (n**2) + n
    
    # read through the file using csv reader, delimited by the commas and quotechars
    # count the triangle words one by one
    count = 0
    with open("problem0042.txt", newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        for row in reader:
            for word in row:
                count += triangle_number(word_score(word))
    return count

def solution0043() -> int:
    """ sum of all 0 to 9 pandigital numbers with special property """
    # iterate over the 10! numbers that are 0 to 9 pandigital
    # check for each of these substring properties, starting with 
    # 17 for d8d9d10
    
    # groupings of sub-string divisibility to check for
    groupings = [
        (7, 10, 17),
        (6, 9, 13),
        (5, 8, 11),
        (4, 7, 7),
        (3, 6, 5),
        (2, 5, 3),
        (1, 4, 2)
    ]
    total = 0
    
    # loop through all permuations of 0 to 9 pandigital numbers
    for perm in permutations(range(10)):
        # create the string
        num = "".join(str(i) for i in perm)
        # loop through the groupings of sub-strings to check
        fail = False
        for start, end, divisor in groupings:
            # break early if a check fails
            if not int(num[start:end]) % divisor == 0:
                fail = True
                break
        # if the current pan-digital passes all of the tests,
        # then include it in the sum
        if not fail:
            total += int(num)
    
    return total

from math import sqrt
from heapq import heappush, heappop, heapify
def solution0044() -> int:
    """ Return the minimzed value of D for pentagonal numbers
    where   Py+Px = Pa
    and     Py-Px = D
    
    Complete this by maintaining a heap with the smallest difference
    between pentagonal numbers. Slow runtime, but proven global minimum answer
    """
    
    @cache
    def pent(n: int) -> int:
        """ Return the nth pentagonal number """
        return n * (3*n - 1) // 2

    # After some algebraic transformations of the constraints, the solution is related to the
    # case where P_a and P_b have a difference that is equal to 2 * P_x, and P_b is minimized
    
    # in this case, P_x + P_b is equal to P_y
    
    def ispentagonal(k: int) -> bool:
        """ returns if a number k is a pentagonal number """
        return ((1 + 24*k)**0.5 + 1) % 6 == 0
    
    # solution method: loop with a generator of sorts...
    # yield the next largest difference between pentagonal numbers
    # if that difference is a pentagonal number, then check if the sum is also
    # pentagonal. If the sum is a pentagonal, then return
    
    # one option is to maintain a heap that contains the position difference between
    # x and y, and the next item in that spacing.
    # the heap should only have the next spacing added to the list when the previous threashold
    # is broken
    # i.e. heap starts [(diff=4, P_b=P_1, spacing=1)]
    # then it becomes [(7, P_2, 1), (11, P_1, 2)]
    # basically, if the popped item has P_1, add an additional item to the heap for spacing n + 1
    
    pq = [(4,1,1)]
    while True:
        # retrieve the next lowest difference from the heap
        diff, i, spacing = heappop(pq)
        
        # break the loop if the properties hold        
        if ispentagonal(diff) and ispentagonal(pent(i) + pent(i+spacing)):
            break
        
        # do logic to update the heap with the next values
        heappush(pq, (pent(i+1+spacing) - pent(i+1), i+1, spacing))
        # on first index of a spacing, create the next index in the heap
        if i == 1:
            heappush(pq, (pent(i+1+spacing) - pent(1), 1, spacing+1))

    # print(len(pq))
    return diff
        
def solution0045() -> int:
    """ Find the next triangle number that is also pentagonal and hexagonal """
    def ispentagonal(k: int) -> bool:
        """ returns if a number k is a pentagonal number """
        return ((1 + 24*k)**0.5 + 1) % 6 == 0
    def ishexagonal(k: int) -> bool:
        return ((1 + 8*k)**0.5 + 1) % 4 == 0
    def triangle(n: int) -> int:
        """ Return the nth triangle number """
        return (n**2 + n) // 2
    curr = 286
    while True:
        t = triangle(curr)
        if ispentagonal(t) and ishexagonal(t):
            break
        curr += 1
    
    return t

def solution0046() -> int:
    """ Return the first composite odd number that cannot be
    expressed as the sum of a prime and 2x a square """
    def sieve_of_eratosthenes(n: int) -> list[int]:
        """Return all prime numbers up to n (inclusive) using the Sieve of Eratosthenes."""
        if n < 2:
            return []

        # Boolean array where index = number, True = prime candidate
        sieve = [1] * (n + 1)
        sieve[0] = sieve[1] = 0  # 0 and 1 are not prime

        # Cross out non-primes
        p = 2
        while p * p <= n:
            if sieve[p]:
                for multiple in range(p * p, n + 1, p):
                    sieve[multiple] = 0
            p += 1

        # Extract primes
        return sieve
    
    limit = 10000
    primes = sieve_of_eratosthenes(limit)
    squares = [2*i**2 for i in range(1, floor(limit**0.5) + 1)]
    # loop through the primes, and then nested loop through the 2x squares
    for i in range(len(primes)):
        if primes[i] < 1:
            continue
        
        for y in squares:
            s = i + y
            # reduce the prime value for all found componsite numbers
            if s <= limit and primes[s] < 1:
                primes[s] -= 1
    
    # loop through the primes list and report the first composite number that did not occur
    for i in range(11,len(primes),2):
        if primes[i] == 0:
            return i
    return -1
    

def solution0047() -> int:
    """ First four consecutive integers to have four distinct prime factors each
    """
    # create a function that counts distinct prime factors
    @cache
    def cf(n: int) -> int:
        """ Returns the number of distinct prime factors """
        count = 0
        for divisor in range(2,floor(n**.5) + 1):
            factor_found = False
            while n % divisor == 0:
                n //= divisor
                factor_found = True
            count += factor_found
        return count + (n > 1)

    # for some limit n, check if n and n + 2 have 4 prime factors
    # if n and n + 2 have 4 prime factors, then check n-1, n+1, and n+3
    
    limit = 1000000
    k = 7
    c = 4
    while k < limit:
        if cf(k) == c and cf(k+1) == c and cf(k+2) == c and cf(k+3) == c:
            return k
        k += 1
    return -1

def solution0048() -> int:
    """ Return the last 10 digits of the series n**n from n=1 to n=1000 """
    # come up with an efficient way to calculate the last 10 digits of each
    # element, then add them together
    MOD = 10**10
    
    def pow(base: int, exp: int, mod: int) -> int:
        """ Returns the result base**exp modulo mod """
        base %= mod
        result = 1
        while exp > 0:
            if exp & 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp >>= 1
        return result

    total = 0
    for i in range(1, 1001):
        total = (total + pow(i, i, MOD)) % MOD
    return total

def solution0049() -> int:
    """ Returns the 12 digits formed by combining 3 4-digit numbers that follow
    the constraints in the problem statement """
    def sieve_of_eratosthenes(n: int) -> list[int]:
        """Return all prime numbers up to n (inclusive) using the Sieve of Eratosthenes."""
        if n < 2:
            return []

        # Boolean array where index = number, True = prime candidate
        sieve = [1] * (n + 1)
        sieve[0] = sieve[1] = 0  # 0 and 1 are not prime

        # Cross out non-primes
        p = 2
        while p * p <= n:
            if sieve[p]:
                for multiple in range(p * p, n + 1, p):
                    sieve[multiple] = 0
            p += 1

        # Extract primes
        return [p for p, isprime in enumerate(sieve) if isprime]
    from collections import Counter
    def are_perms(a: int, b: int, c: int) -> bool:
        """ Returns true if the numbers are permutations of each other """
        return Counter(str(a)) == Counter(str(b)) == Counter(str(c))
    
    # generate the primes between 1 and 10,000
    primes = sieve_of_eratosthenes(10000)
    
    # Find the two 3 set of terms which are prime and share a difference
    s = set(primes)
    
    # loop through the primes in reverse, checking for each differences
    count = 0
    for i in range(len(primes)-1, 0, -1):
        for j in range(i-1, -1, -1):
            if count == 2:
                break
            diff = primes[i] - primes[j]
            if primes[j] - diff in s and are_perms(primes[j]-diff, primes[j], primes[i]):
                return ''.join([str(primes[j]-diff), str(primes[j]), str(primes[i])])
    return ""
    

def solve_0040_thru_0049():
    test()
    # print('solve 40: ', solution0040())
    # print('solve 41: ', solution0041())
    # print('solve 41 improved: ', solution0041_improved())
    # print('solve 42: ', solution0042())
    # print('solve 43: ', solution0043())
    # print('solve 44: ', solution0044())
    # print('solve 45: ', solution0045())
    # print('solve 46: ', solution0046())
    # print('solve 47: ', solution0047())
    # print('solve 48: ', solution0048())
    print('solve 49: ', solution0049())

def test():
    """ run doctests - practice coding """
    import doctest
    # this will run all doctests in the module
    doctest.testmod()
    # optionally run doctests for a specific function
    # doctest.run_docstring_examples(solution0041, globals())
    
if __name__ == "__main__":
    solve_0040_thru_0049()