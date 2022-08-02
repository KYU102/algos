

def findMaxOnes(nums):

    max = 0
    counter = 0

    for num in nums:
        if num == 1:
            counter +=1 
        if num == 0:
            if counter > max:
                max = counter
            counter = 0
    
    if counter > max:
        return counter

    return max

print(findMaxOnes([1]))
