def pivotIndex(nums):
    S = sum(nums)
    leftsum = 0

    for i, x in enumerate(nums):
    # enumerate will index(i) and take the val(x) and create a tuple

        if leftsum == (S - leftsum - x):
        # if the sum of the left is equal to the total - the left and the current index value
        # because you dont include the pivot value 
            return i
        leftsum += x
        # ad the sum as we iterate up through the left 
    return -1
print(pivotIndex([1,7,3,6,5,6]))