def containsDuplicate(nums):
    nums.sort()

    for num in range(len(nums)-1):
        if nums[num] == nums[num+1]:
            return True

    return False
    