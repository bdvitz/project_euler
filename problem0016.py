# projecteuler.net solutions
def solution0016(n = 1000):
    """ return the sum of digits in the number 2**n """
    num = 2**n
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total
    
if __name__ == "__main__":
    print(solution0016())