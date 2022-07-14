


def removeDuplicates(nums):
    
    for i in range(len(nums) - 2):
        if (nums[i] == nums[i + 1]):
            nums.pop(i + 1)
            i -= 1

    return nums


print(removeDuplicates([1,1,2,3,4,5,5,5,5,5,5]))
