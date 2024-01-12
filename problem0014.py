# projecteuler.net solutions
def solution0014(limit = 1000000):
    """ return the largest collatz sequence starting number less than limit """
    result = 0
    best =  0
    for i in range(1, limit):
        curr = len_seq(i)
        if result < curr:
            result = curr
            best = i
    
    return result, best

def len_seq(start = 1):
    count = 1
    while start != 1:
        if start % 2 == 0:
            start >>= 1
        else:
            start += (start<<1) + 1
        count += 1
    
    return count
    
if __name__ == "__main__":
    n = 1000000
    # print('length: ', len_seq(999999))
    # print(solution0014(n))
    print(solution0014())