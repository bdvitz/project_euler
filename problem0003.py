# projecteuler.net solutions
def solution0003(input: int):
    """ return largest prime factor """
    assert input > 1, 'cannot have an input smaller than +2'
    
    # divide all factors of 2
    largest = -1
    while input % 2 == 0:
        largest = 2
        input //= 2
    
    # divide by all other odd nubmers between 3 and the sqrt of input
    for i in range(3,int(input**.5)+1,2):
        while input % i == 0:
            largest = i
            input //= i
    
    # return the largest prime factor if input is not prime itself
    # otherwise, return input
    return largest if input < 2 else input
    
if __name__ == "__main__":
    print(solution0003(600851475143))