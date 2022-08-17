
def twoSum(nums, target):

    hashMap = {}
    res = []

    for i in nums:
        if target - i > 0:
            hashMap[i] = hashMap.get(i, target - i)
    
    for key in hashMap:
        res.append(nums.index(key))
    
    return hashMap

print(twoSum([3,2,4],6))