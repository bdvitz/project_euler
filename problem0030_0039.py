# solutions 30 through 39
def solution0030(power = 5) -> int:
    """ Returns the sum of all the numbers that can be written as the sum of 'power' powers of their digits
    Examples:
        >>> solution0030(4)
        19316
    """
    # check if the brute force solution is sufficient
    # check all numbers from 10 through 9**power * (power+1) to see if the number == the sum of digits to power
    good = 0
    for i in range(10, 9**power * (power+1)):
        total = 0
        curr = i
        while curr > 0:
            # retrieve the first digit
            curr, digit = divmod(curr, 10)
            # add the current digit**power to the total
            total += digit**power
            # check for early exit
            if i < total: break
        # check if the sum of digits to power is the original number
        if i == total:
            good += total
    # return the sum of numbers with this property
    return good

def solution0031(target = 2) -> int:
    """ Return the number of ways to form target value in pounds out of the 8 coin denominations """
    target *= 100 # convert from pounds to pence
    denominations = [1, 2, 5, 10, 20, 50, 100, 200]
    # employ 2d dp solution from 0 through the target value in pence
    n = target + 1
    dp = [1] * n
    # loop through all denominations and all indeces in the list
    for d in denominations[1:]:
        # only increment to indeces 'i' that are in the range of dp
        for i in range(n-d):
            dp[i+d] += dp[i] # add a way to get to dp[i+d] from dp[i] in value
    # return the final value
    return dp[-1]

def solution0032(n = 9) -> int:
    """ Return the sum of all products whose multiplicand/multiplier/product identity
    can be written as a 1 through 9 pandigital """
    
    # there are n! possible orderings of n digits. There are (n-1)C2 unique splits = (n-1)! / [2!*(n-3)!]
    # in the case of n = 9, this is only 28 * 9! = 28 * 362,880 = 10,160,640
    # brute force seems acceptable
    # first, efficiently generate all unique orderings of digits 1 through 9
    # second, check all 28 splits for multiplicand/multiplier/product identity
    
    # create a generator function that yields the next unique ordering of digits in a list
    curr = []
    def backtrack(digs: list):
        # base case for generator
        if not digs:
            yield curr[:]
        # still digits left, add digits to current and continue backtrack
        for i, d in enumerate(digs):
            # add the current digit
            curr.append(d)
            # create a new list without the current digit
            for ans in backtrack(digs[:i] + digs[i+1:]):
                yield ans
            # remove the current digit
            curr.pop()

    
    products = set() # do not double count products
    for unique_ordering in backtrack(list(range(1,n+1))):
        # identify the left and right splits
        for left in range(1, n-2):
            for right in range(left+1, n-1):
                a = list2num(unique_ordering[:left])
                b = list2num(unique_ordering[left:right])
                prod = list2num(unique_ordering[right:])
                if a * b == prod:
                    products.add(prod)
        # print(unique_ordering)
    
    # print(products)
    return sum(products)

def list2num(digs: list):
    """ convert a list of digits to numbers """
    tens = 1
    res = 0
    while digs:
        res += tens*digs.pop()
        tens *= 10
    return res

def solution0033():
    """ Return the denominator of the product of
    four non-trivial curious fractions in lowest common terms """
    # first return the 4 fractions, then calculate denominator by hand
    # 4 possible ways to add a digit to fractions with 1 digit in numerator and denominator
    # O(n^2) ways to make a single digit numerator and denominator less than 1
    # check all of them
    
    def check(n, d, dig, target):
        """ check all 4 possible ways to add digit to numerator and denominator """
        # case 1, before both
        if int(dig + n) / int(dig + d) == target:
            return True
        # case 2, before numerator and after denominator
        if int(dig + n) / int(d + dig) == target:
            return True
        # case 3, after numerator and before denominator
        if int(n + dig) / int(dig + d) == target:
            return True
        # case 4, after both
        if int(n + dig) / int(d + dig) == target:
            return True
        return False
    
    results = []
    # list all non-zero digits
    numbers = [str(i) for i in range(1,10)]
    # loop through single digit denominators
    for d in range(len(numbers)):
        denominator = numbers[d]
        # loop through lower than denominator nonzero numerators because the fraction is less than zero
        for n in range(d):
            numerator = numbers[n]
            # determine the target fraction after adding a digit to both numerator and denominator
            target = int(numerator) / int(denominator)
            # for each numerator denominator pair, check 4 possible double digit fractions
            for digit in numbers:
                # if there exists a result, add the numerator denominator pair to a results list for return
                if check(numerator, denominator, digit, target):
                    results.append((numerator, denominator, digit))
    return results

def solution0034() -> int:
    """ Return the sum of all numbers which are equal to the sum of the factorial of their digits """
    f = 1
    factorials = [1]
    for i in range(1,10):
        f *= i
        factorials.append(f)
    
    # print(factorials)
    
    results = []
    def backtrack(curr: int, fact_sum: int, depth: int):
        # base case: process calculation
        if depth == 0:
            # if curr % 10000 == 0: print(curr)
            if curr == fact_sum:
                results.append(curr)
            return
        
        # other cases
        curr *= 10
        for i in range(10):
            # increment the number by shifting existing digits and adding the new digit
            curr += i
            # only add to the factorial sum if not a leading zero
            if curr > 0:
                fact_sum += factorials[i]
            # backtrack
            backtrack(curr, fact_sum, depth - 1)
            # undo the additions
            if curr > 0:
                fact_sum -= factorials[i]
            curr -= i
    
    backtrack(0, 0, 5) # check range [0, 10**(5+1)) where 5 is the depth or number of digits
    return sum(results[3:]) # ignore, 0!, 1! and 2!

def solution0035(n = 1000000) -> int:
    """ return the count of circular primes below one million """
    from math import log10
    # implement the sieve of erotosthenes
    is_prime = [True] * n
    for k in range(2, int(n**.5)+1):
        if is_prime[k]:
            for multiple in range(k * k, n, k):
                is_prime[multiple] = False
    
    # of the 5 odd digits, choose subsets of them with replacement
    # to check for circular primes below one million
    # create a generator for permutations with replacement and without repeats
    # possible to avoid checks of rotated patterns? not worth my time right now
    curr = []
    # account for multiple counting of circular numbers that have 'k' digits
    count = [0] * (int(log10(n)) + 1)
    
    def backtrack(depth: int):
        # base case
        if depth == 0:
            if check(curr):
                count[len(curr)] += 1
            return
        
        # not base case, seek digits
        for d in range(1,10,2):
            curr.append(d)
            backtrack(depth - 1)
            curr.pop()
        
    def check(digits: list) -> bool:
        """ Return True if the digits form a circular prime """
        for i in range(len(digits)):
            if not is_prime[list2num(digits[i:] + digits[:i])]:
                return False
        return True

    # backtrack for all length integers up to the threshold 'n'
    for i in range(1, int(log10(n))+1):
        backtrack(i)
    
    return sum(count)

def solution0036(n = 1000000):
    """ Sum of numbers below n are palindromic in base 10 and base 2 """
    from math import log10
    # helper functions for palindrome integer creation
    def create_even_palindrome(digits: list) -> int:
        """ Return an even length palindrome int by connecting the digits """
        return list2num(digits + digits[::-1])
    def create_odd_palindrome(digits: list) -> int:
        """ Return an odd length palindrome int by connecting the digits """
        return list2num(digits + digits[-2::-1])
    def is_binary_palindrome(num: int) -> bool:
        """ Return true if the integer is a binary palindrome """
        s = bin(num)[2:]
        return s == s[::-1]
    
    # sum the values which are palindromes in both base 10 and base 2
    total = 0
    # update n to be sqrt(n) for the case where n = 1,000,000
    n = int(n**.5)
    # results = []
    for i in range(n):
        digits = [int(c) for c in str(i)]
        even = create_even_palindrome(digits)
        if is_binary_palindrome(even):
            total += even
            # results.append(even)
        odd = create_odd_palindrome(digits)
        if is_binary_palindrome(odd):
            total += odd
            # results.append(odd)
    # print(results)
    return total

def solution0036_first_look(n = 1000000):
    """ first look at the problem, focused on counting the number of palindromes in each base """
    # first questions first, are there more palindromes < n in base 10 or base 2?
    # 2 ^ 20 is approximately 1 million, slightly larger
    # 2 ^ 20 has 21 binary digits. Therefore numbers up to 1 million
    # can be expressed with 20 binary digits
    
    # the number of palindromes with 20 0's and 1's can be expressed by the number of unqiue half-length
    # combinations that are not mirror symmetric
    # Therefore, there are (2^10) unique even length palindromes
    # additionally, there will be odd palindromes of length 9 with an extra 0 or 1 to join them
    # therefore, in total, (2^10) + (2^9 * 2) palindromes or (2^11)
    # total: 2^11 = 2048
    
    # for base 10 numbers less than 1 million:
    # there are 10 digits and half length 3
    # 10^3 possible selections for palindromes of length 6 or even lower than 6
    # 10^2 first two digits * 10 middle digits selections for palindromes of length 5 or odd lower than 5
    # total: 2 * 10^3 = 2000...zero was double counted here though
    
    # count number of palindromes up to n
    def is_palindrome(nums: list) -> bool:
        i = 0
        while i < len(nums) and nums[i] == 0:
            i += 1
        test = nums[i:]
        return test == test[::-1]
        
    
    curr = []
    count = 0 # count 0 as a palindrome without leading zeros
    def backtrack(depth: int):
        nonlocal count
        if depth == 0:
            if is_palindrome(curr):
                # print(curr)
                count += 1
            return
        
        for i in range(10):
            curr.append(i)
            backtrack(depth - 1)
            curr.pop()
    
    backtrack(6)
    
    return count
    
def solution0037(n = 1000000) -> int:
    """ Find the sum of eleven truncatable primes from left to right and right to left """
    
    # sieve of erotosthenese
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, n):
        if is_prime[i]:
            for multiple in range(i * i, n, i):
                is_prime[multiple] = False
    
    def truncatable(digits: str, direction: bool) -> bool:
        """ Return if a list of digits is a truncatable prime in both directions """
        # base case
        if len(digits) == 1:
            return is_prime[int(digits[0])]
        
        # longer than 1 digit string
        if not is_prime[int(''.join(digits))]:
            return False
        
        # check children
        if direction:
            if truncatable(digits[1:], direction):
                return True
        else:
            if truncatable(digits[:-1], direction):
                return True
        return False
        
    # create a generator to efficiently grab the next prime
    def get_primes():
        """ Generator function for primes """
        nonlocal n
        for i in range(10,n):
            if is_prime[i]:
                yield i
    
    results = []
    # check all of the primes generated
    for p in get_primes():
        digits = str(p)
        if truncatable(digits, True) and truncatable(digits, False):
            results.append(p)
    
    print(results)
    return sum(results)

def solve_0030_thru_0039():
    # test()
    # print('solve 30: ', solution0030())
    # print('solve 31: ', solution0031())
    # print('solve 32: ', solution0032())
    # print('solve 33: ', solution0033())
    # print('solve 34: ', solution0034())
    # print('solve 35: ', solution0035())
    # print('solve 36: ', solution0036())
    print('solve 37: ', solution0037())

def test():
    """ run doctests - practice coding """
    import doctest
    # this will run all doctests in the module
    doctest.testmod()
    # optionally run doctests for a specific function
    # doctest.run_docstring_examples(solution0031, globals())
    
if __name__ == "__main__":
    solve_0030_thru_0039()