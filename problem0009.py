# projecteuler.net solutions
def solution0009_brute_force() -> int:
    """ returns the product abc for a pythagorean triplet where a+b+c == 1000 """
    target = 1000
    for c in range(target-2,0,-1):
        # a+b = target-c = diff
        diff = target-c
        square = c**2
        for a in range(1,diff):
            b = diff - a
            # assert a+b+c == target
            if a**2 + b**2 == square:
                return a*b*c
    return -1
    
if __name__ == "__main__":
    print(solution0009_brute_force())