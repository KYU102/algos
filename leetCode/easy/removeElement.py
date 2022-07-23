


def removeElement(nums, val):
    counter = 0
    for i in nums:
        if i == val:
            counter += 1
    
    return [counter, nums]


print(removeElement([3,2,2,3], 3))
