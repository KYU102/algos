
def findLongest(nums):
    
    pointer = 0
    longest = 1
    counter = 1

    while pointer != len(nums) - 1:

        if nums[pointer] < nums[pointer + 1]:
            counter += 1
        
        else: 
            longest = max(longest, counter)
            counter = 1

        pointer += 1

    
    return max(longest, counter)


print(findLongest([1,3,5,7]))


