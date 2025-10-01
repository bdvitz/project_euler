from bisect import bisect_right

# projecteuler.net solutions
def solution0017(n = 1000):
    """ total number of letters used to write out 1 through n 
    
    simply count the instances of the words
    one two three four five six seven eight nine ten
    eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen
    twenty thirty forty fifty sixty seventy eighty ninety
    one hundrend, etc.
    
    coding solution:
    - create a sorted list and dictionary containing the numbers for these words
    - traverse in descending order, checking if the number can be used
    """
    names = {
        1000: (11, "onethousand"),
        900: (11, "ninehundred"),
        800: (12, "eighthundred"),
        700: (12, "sevenhundred"),
        600: (10, "sixhundred"),
        500: (11, "fivehundred"),
        400: (11, "fourhundred"),
        300: (12, "threehundred"),
        200: (10, "twohundred"),
        100: (10, "onehundred"),
        90: (6, "ninety"),
        80: (6, "eighty"),
        70: (7, "seventy"),
        60: (5, "sixty"),
        50: (5, "fifty"),
        40: (5, "forty"),
        30: (6, "thirty"),
        20: (6, "twenty"),
        19: (8, "nineteen"),
        18: (8, "eighteen"),
        17: (9, "seventeen"),
        16: (7, "sixteen"),
        15: (7, "fifteen"),
        14: (8, "fourteen"),
        13: (8, "thirteen"),
        12: (6, "twelve"),
        11: (6, "eleven"),
        10: (3, "ten"),
        9: (4, "nine"),
        8: (5, "eight"),
        7: (5, "seven"),
        6: (3, "six"),
        5: (4, "five"),
        4: (4, "four"),
        3: (5, "three"),
        2: (3, "two"),
        1: (3, "one"),
    }
    nums = sorted(names.keys())
    
    def cache(fn: callable):
        d = {}
        def helper(*args):
            if args in d:
                return d[args]
            ans = fn(*args)
            d[args] = ans
            return ans
        return helper
    
    
    @cache
    def num_letters(start: int):
        # base case
        if start == 0:
            return (0, '')
        
        # retrieve the number less than or equal to nums
        num = nums[bisect_right(nums, start)-1]
        
        # generate the number of letters using recursion
        ans, letters = num_letters(start-num)
        if (start % 100 != 0) and (100 <= start <= 999): # accounting for the word 'and'
            return (3 + names[num][0] + ans, names[num][1] + 'and' + letters)
        else:
            return (names[num][0] + ans, names[num][1] + letters)
    
    return sum([len(num_letters(i)[1]) for i in range(1,n+1)])
    # return [num_letters(i)[1] for i in range(1,n+1)]

def write_to_file(filename: str, words: list):
    n = len(words)
    with open(filename, "w") as file:
        for i in range(1,n+1):
            file.write(str(i) + ": " + words[i-1] + "\n")

if __name__ == "__main__":
    n = 1000
    ans = solution0017(n)
    print(ans)
    # write_to_file("my_list.txt", ans)
    