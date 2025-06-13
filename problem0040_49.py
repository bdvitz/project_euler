
def solution0040(power = 7) -> int:
    """ Return the product of dn (i.e. PI [dn]) for n from 10^0 to 10^(power-1) 
    in the irrational decimal fraction that is created by concatenating
    the positive integers
    
    >>> solution0040(2)  # 0.1234567891 has a 1 in both n=1 and n=10 positions. d1 * d10 = 1
    1
    """
    product = 1
    
    # This solution requires an algorithm to efficiently calculate the nth digit
    # simply count the number of digits in the current number range using math
    # the number range increases by 10x every power of 10
    
    def calculateDigit(n: int) -> int:
        """ Returns the nth digit in the sequence """
        position = 1
        power = 0
        # increase the power and position if the current upper bound is less than n
        while True:
            lower, upper = 10**power, 10**(power+1)-1
            
            # determine the number of numbers in the range
            number_count = upper - lower + 1
            
            # determine the number of digits in the range
            digit_count = number_count * (power + 1)
            
            # increase the power
            power += 1
            
            # increase the position if it does not skip past n
            # otherwise, break the loop and find n in the position range
            if n >= position + digit_count:
                position += digit_count
            else:
                break
        
        # now the nth digit falls in the range [position, position + digit_count]
        # the number containing the nth digit and the digit itself
        # can be determined with simple math
        number_index = (n-position) // power
        
        # find the number containing this special digit
        number = lower + number_index
        
        # retrieve the correct digit from the number
        return int(str(number)[(n-position) % power])
    
    # for debugging
    # for i in range(20):
    #     print(calculateDigit(i))
    
    for exponent in range(power):
        ans = calculateDigit(10**exponent)
        product *= ans
        
    return product

def solve_0040_thru_0049():
    test()
    print('solve 40: ', solution0040())
    # print('solve 41: ', solution0041())
    # print('solve 42: ', solution0042())
    # print('solve 43: ', solution0043())
    # print('solve 44: ', solution0044())
    # print('solve 45: ', solution0045())
    # print('solve 46: ', solution0046())
    # print('solve 47: ', solution0047())
    # print('solve 48: ', solution0048())
    # print('solve 49: ', solution0049())

def test():
    """ run doctests - practice coding """
    import doctest
    # this will run all doctests in the module
    doctest.testmod()
    # optionally run doctests for a specific function
    # doctest.run_docstring_examples(solution0041, globals())
    
if __name__ == "__main__":
    solve_0040_thru_0049()