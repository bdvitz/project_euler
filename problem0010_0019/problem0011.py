from math import prod

# projecteuler.net solutions
def solution0011(nums = None, length = 4):
    """ Return the greatest product of four adjacent numbers in the same direction 
    from the provided 20 x 20 grid of numbers within problem0011.txt"""
    # retrieve the 20x20 grid of numbers from the text file
    if nums is None:
        with open('problem0011.txt') as file:
            nums = [list(int(num) for num in line.split()) for line in file.read().split('\n')]
    
    # optionally use dp to improve runtime by 4x
    # brute force solution first
    
    # size of the grid
    rows, cols = len(nums), len(nums[0])
    
    # define the vectors of neighboring cells using range(length)
    vec_horz = [(0,i) for i in range(length)]
    vec_vert = [(i,0) for i in range(length)]
    vec_diag_dr = [(i,i) for i in range(length)]
    vec_diag_dl = [(i,-i) for i in range(length)]
    
    # define the product calculation
    def product(nums: list, row: int, col: int, vectors: list) -> int:
        """ return the product of len(vectors) values from nums """
        return prod(nums[row+i][col+j] for i,j in vectors)
    
    best = 0
    # check products with nested for loop through all of grid
    for row in range(rows):
        for col in range(cols):
            # check horizontal groupings if columns exist to the right
            if col <= cols-length:
                curr = product(nums, row, col, vec_horz)
                best = max(best, curr)
                    
            # check vertical groupings if rows exist below
            if row <= rows-length:
                curr = product(nums, row, col, vec_vert)
                best = max(best, curr)
            
            # check diagonal groupings if rows and columns exist diagonally down and right
            if (col <= cols-length) and (row <= rows-length):
                curr = product(nums, row, col, vec_diag_dr)
                best = max(best, curr)
            
            # check diagonal groupings if rows and columns exist diagonally down and left
            if (col >= length-1) and (row <= rows-length):
                curr = product(nums, row, col, vec_diag_dl)
                best = max(best, curr)
    
    return best
    
if __name__ == "__main__":
    print(solution0011())