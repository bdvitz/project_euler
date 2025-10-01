# projecteuler.net solutions
def solution0012_brute_force(divisors = 500, stop = 10000):
    """ return the first triangle number with n+1 divisors
    
    search triangle numbers using the closed form solution
    use helper function to determine the number of divisors a number has
    can be optimized with a better understanding of the prime numbers
    """
    
    def num_divisors(num: int) -> int:
        if num == 1:
            return 1
        result = 2
        for i in range(2, int(num**0.5)):
            if num % i == 0:
                result += 2
        if int(num**0.5)**2 == num:
            result += 1
        return result
    
    def triangle_term(n: int) -> int:
        """ return the nth triangle number term """
        return ((n+1)*n) // 2
    
    for i in range(1,stop):
        if num_divisors(triangle_term(i)) > divisors:
            return triangle_term(i)
    return -1
    
    # # locate a value above the limit divisors
    # for i in range(1,10001,step):
    #     if num_divisors(triangle_term(i)) > divisors:
    #         break
    
    # # i is greater than or equal to the target
    # target = divisors + 1
    # # bisect_left binary search to the target
    # low, high = 1, i
    # while low <= high:
    #     mid = (low + high) // 2
    #     if num_divisors(triangle_term(mid)) < target:
    #         low = mid + 1
    #     else:
    #         high = mid - 1
    # # low is the triangle term that is the answer
    # return triangle_term(low)
    
if __name__ == "__main__":
    n = 500
    search_limit = 100000
    # 36, 1, 2, 3, 4, 6, 9, 12, 18, 36
    # n = 500
    print(solution0012_brute_force(n,search_limit))