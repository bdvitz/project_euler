# projecteuler.net solutions
def solution0018(filename: str):
    """ maximum path sum I: calculate the maximum total from top to bottom using dp """
    with open(filename) as file:
        nums = [list(int(num) for num in line.split()) for line in file.read().split('\n')]
    
    # loop through the rows in nums, modifying the rows in place
    for i in range(1, len(nums)):
        for j in range(len(nums[i])):
            # for j == 0 or j == len(nums[i]-1), there is only one row above
            if j == 0:
                nums[i][j] += nums[i-1][j]
            elif j == len(nums[i])-1:
                nums[i][j] += nums[i-1][j-1]
            # otherwise, take the max of the previous row values above this location
            else:
                nums[i][j] += max(nums[i-1][j-1], nums[i-1][j])
    
    return max(nums[-1]) # maximum in the final row
    
if __name__ == "__main__":
    print(solution0018('problem0018.txt'))