def mutateArray(nums):

    res = []

    for i in range(len(nums)-1):
        if i ==0:
            res.append(nums[0]+ nums[1])
        if i == len(nums)-1:
            res.append(nums[-1]+nums[-2])
        else:
            res.append(sum(nums[i:i+3]))

    return res

print(mutateArray([4,0,1,-2,3]))
