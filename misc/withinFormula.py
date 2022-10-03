def isTrue(nums,left,right):
    arr = []
    res = []

    for i in range(left,right):
        arr.append(i)

    for i in range(len(nums)):
        if nums[i]/(i+1) in arr:
            res.append(True)
        else:
            res.append(False)

    return res

print(isTrue([8,5,6,16,5],1,3))