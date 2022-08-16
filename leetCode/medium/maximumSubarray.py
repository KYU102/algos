from sys import maxsize


def maxSub(nums):

    max = 0 
    if len(nums) == 1 and nums[0] > max:
        return nums[0]
    for i in range(len(nums) - 1) :
        for j in range(i+ 1, len(nums) - 1):
            if sum(nums[i:j]) > max:
                max = sum(nums[i:j])
    
    return max
    

print(maxSub([1]))