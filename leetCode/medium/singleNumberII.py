

def singleNumber(nums):
    nums.sort()

    if len(nums) == 1:
        return nums[0]
    
    if nums[-1] != nums[-3]:
        return nums[-1]
        
    for number in range(0, len(nums) - 2, 3):
        if nums[number] != nums[number+2]:
            return nums[number]
        

print(singleNumber([1,1,1,2,2,2,3,4,4,4]))