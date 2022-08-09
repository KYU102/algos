
def addToArrayForm(nums, k):

    num = nums[0]
    print(num)
    multiplier = 1

    for i in range(0, len(nums) - 1, -1):
        num = num + (i * multiplier)
        multiplier *= 10
    
    return k

print(addToArrayForm([1,2,0,0],34))
