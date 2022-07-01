


def thirdMax(nums):
    thirdLargest = 0
    count = 1
    nums.sort()
    
    while count < 3:
        if nums[count] > nums[count-1]:
            thirdLargest = nums[count + 1]
            count+=1
        return thirdLargest

tester = [1,4,5,2]
print(thirdMax(tester))