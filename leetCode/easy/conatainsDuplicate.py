
def containsDuplicate(nums):

    if len(nums) < 2:
        return False
    
    nums.sort()

    for num in range(len(nums) - 1):
        if nums[num] == nums[num + 1]:
            return True

    return False