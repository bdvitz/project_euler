# projecteuler.net solutions
def solution0015(m = 20, n = 20):
    """ return the number of paths from top left to bottom right of m by n grid
    
    can only move right or down 
    m: rows (of nodes)
    n: columns (of nodes)"""
    
    # must add one to match problem intent
    m += 1
    n += 1
    
    dp = [1] * (n+1)
    dp[0] = 0
    for row in range(m-1):
        for col in range(1,n+1):
            dp[col] += dp[col-1]
    
    return dp[n]
    
if __name__ == "__main__":
    print(solution0015())