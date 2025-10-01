# projecteuler.net solutions
def solution0006_brute_force(n: int):
    """ return the difference of 1^2 + 2^2 + ... +(n-1)^2 + n^2 and (1+2+...+(n-1)+n)^2 """
    return sum(i for i in range(1,n+1))**2 - sum(i**2 for i in range(1,n+1))
    
if __name__ == "__main__":
    print(solution0006_brute_force(100))