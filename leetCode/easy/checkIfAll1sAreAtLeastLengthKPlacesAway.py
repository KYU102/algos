def kLengthApart(nums,k):
    count = k

    for num in nums:
        if num == 1:
            if count < k:
                return False
            count = 0 
        else:
            count+=1

    return True



print(kLengthApart([1,0,0,0,1,0,0,1],2))