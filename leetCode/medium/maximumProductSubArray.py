import math
def maxProduct(nums):
    large = 0

    if len(nums) == 1:
        return nums[0]

    for i in range(len(nums)):
        for j in range(i+1,len(nums)+1):
            large = max(math.prod(nums[i:j+1]), large)
    
    return max(large, max(nums))

print(maxProduct([[-2,0,-1]]))
