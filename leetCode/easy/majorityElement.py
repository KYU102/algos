def majorityElement(nums):
    
    counter = {}

    for num in nums:
        counter[num] = counter.get(num,0) + 1

    for key, val in counter.items():
        if val > len(nums)//2:
            return key
    
