# projecteuler.net solutions

from math import factorial

def solution0005_brute_force(n: int):
    """ returns the smallest positive number evenly divisible by 1 through n """
    for i in range(1,factorial(n)+1):
        if not any(i%j != 0 for j in range(2,n+1)):
            return i
    return -1  
    
def solution0005(n: int):
    """ returns the smallest positive number evenly divisible by 1 through n """
    
    # generate prime factors of numbers from 2 to n
    # multiply the maximum count of each prime factor by each other
    
    def update_factor_counts(num: int) -> None:
        """ update the local list tracking maximum count of prime 
        factors required for a product of the numbers to be divisible by num """
        if num <= 1:
            return
    
        # divide all factors of 2
        count = 0
        while num % 2 == 0:
            num //= 2
            count += 1
        factor_counts[2] = max(factor_counts[2], count)
        
        # divide by all other odd numbers between 3 and the sqrt of input
        for i in range(3,int(num**.5)+1,2):
            count = 0
            while num % i == 0:
                num //= i            
                count += 1
            factor_counts[i] = max(factor_counts[i], count)
        
        if num > 1:
            factor_counts[num] = max(factor_counts[num], 1)
    
    factor_counts = [0] * (n+1)
    for i in range(2,n+1):
        update_factor_counts(i)
    
    # print(factor_counts)
    result = 1
    for factor, count in enumerate(factor_counts):
        if count > 0:
            result *= factor**count
    
    return result
    
if __name__ == "__main__":
    n = 100
    if n <= 10:
        print(solution0005_brute_force(n))
    else:
        print(solution0005_brute_force(10))
    print(solution0005(n))