

def findError(nums):

    error = 0
    correctNum = 0

    for i in range(len(nums) - 1):
        if nums[i] == nums[i +1]:
            error = nums[i]
            correctNum = nums[i] + 1
    return [error, correctNum]
print(findError([1,2,2,4]))
