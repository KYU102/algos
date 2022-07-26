


def singleNumber(nums):
    nums.sort()

    if len(nums) == 1:
        return nums[0]
    
    if nums[-1] != nums[-2]:
        return nums[-1]
        
    for number in range(0, len(nums) - 1, 2):
        if nums[number] != nums[number+1]:
            return nums[number]
        

print(singleNumber([1]))