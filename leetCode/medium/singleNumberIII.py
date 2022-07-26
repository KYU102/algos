


def singleNumber(nums):
    
    nums.sort()
    num1 = 'x'
    num2 = 'x'
    x = 0
    index = 0

    if len(nums) == 2:
        return nums

    if nums[0] != nums[1]:
        num1 = nums[0]
        x +=1
    
    if nums[-1] != nums[-2]:
        num2 = nums[-1]



    for number in range(x, len(nums) - 1, 2):
        if nums[number] != nums[number+1] and num1 == 'x':
            num1 = nums[number]
            index = number + 1
    if x < 1:
        for i in range(index+ 1,len(nums) - 1, 2):
                if nums[i] != nums[i+1]:
                    num2 = nums[i + 1]
    else:
        for i in range(index+ 1,len(nums) - 1, 2):
            if nums[i] != nums[i+1]:
                num2 = nums[i]
            
    
    return [num1, num2]

print(singleNumber([-1638685546,-2084083624,-307525016,-930251592,-1638685546,1354460680,623522045,-1370026032,-307525016,-2084083624,-930251592,472570145,-1370026032,1063150409,160988123,1122167217,1145305475,472570145,623522045,1122167217,1354460680,1145305475]))
