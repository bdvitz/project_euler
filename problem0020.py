# projecteuler.net solutions
from math import factorial
def solution0020(n: int):
    """ Return the sum of the digits in the number 100! """
    n = factorial(n)
    total = 0
    while n > 0:
        n, d = divmod(n, 10)
        total += d
    return total
    
if __name__ == "__main__":
    print(solution0020(100))