# projecteuler.net solutions
def solution0013(nums = None):
    """ Return the first 10 digits of the sum of
    one-hundred 50-digit numbers in solution0013.txt """
    
    if nums is None:
        with open('problem0013.txt') as file:
            nums = [int(line) for line in file.read().split('\n')]
    
    return str(sum(nums))[:10]
    
    
if __name__ == "__main__":
    nums = [12345456236342644,
            23452352345234523,
            23452345423521671]
    # print(solution0013(nums))
    print(solution0013())