def isMajorityElement(nums,target):
    
    counter = 0

    for num in nums:
        if num == target:
            counter+=1
    
    return counter > len(nums)//2

    