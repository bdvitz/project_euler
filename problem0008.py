# projecteuler.net solutions
def solution0008_brute_force(n = 13) -> tuple:
    """ returns the largest product of n adjacent digits in the
    1000 digit number within problem0008.txt """
    
    with open('problem0008.txt') as file:
        contents = ''.join([line.strip() for line in file.readlines()])
    
    assert len(contents) >= n, 'there must be less adjacent digits than the number length'
    
    # create list of digits, order of digits does not matter
    digits = [int(digit) for digit in contents]

    # find largest product from adjacent n digits
    best_product = 0
    location = (0,0)
    product = 1
    i = 0
    for j in range(len(digits)):
        curr = digits[j]
        # check for zeros and skip them
        if curr == 0:
            i = j+1
            product = 1
        else:
            product *= curr
        
        # check for maximum window length
        if i + n - 1 == j:
            if best_product < product:
                best_product = product
                location = (i,j)
            product //= digits[i]
            i += 1
    
    return best_product,digits[location[0]:location[1]+1]
    
if __name__ == "__main__":
    print(solution0008_brute_force())