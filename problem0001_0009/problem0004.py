# projecteuler.net solutions
def solution0004(n: int):
    """ return largest palindrome product of two n-digit numbers """
    
    # brute force solution
    # can be improved by breaking the loops when the new products are less than the maximum
    
    def is_palindrome(num: int):
        if num == 0:
            return True
        
        chars = []
        temp = num
        while temp > 0:
            chars.append(temp%10)
            temp//=10
        
        chars.reverse()
        while chars:
            temp*=10
            temp+= chars.pop()
        
        return temp == num
    
    n = 10**n - 1
    best = 0
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            if is_palindrome(i*j):
                best = max(best, i*j)
    
    return best
    
if __name__ == "__main__":
    print(solution0004(3))