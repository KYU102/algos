


def sumEvenAfterQuesries(nums,queries):
    res = []
    subSum = 0
    for query in queries:
        nums[query[1]] += query[0]
        for num in nums:
            if num%2 == 0:
                subSum+=num
        res.append(subSum)
        subSum = 0
    

    return res

print(sumEvenAfterQuesries([1,2,3,4],[[1,0],[-3,1],[-4,0],[2,3]]))