# projecteuler.net solutions
def solution0002(maximum: int):
    """ sum the even fibonacci terms that do not exceed four million """
    # brute force solution
    a,b = 1,2
    result = 0
    while b <= maximum:
        if b%2==0:
            result += b
        a,b = b,a+b
    return result

if __name__ == "__main__":
    print(solution0002(4000000))