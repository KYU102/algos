
def sortedSquares(nums):
    
    res = []

    for i in nums:
        res.append(i*i)
    
    res.sort()
    return res

print(sortedSquares([-7,-3,2,3,11]))