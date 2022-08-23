
def findLeastNumOfUniqueInts(nums, k):
    dic = {}
    sortedDic = {}
    sortedKeys = sorted(dic, key=dic.get)

    for num in nums:
        dic[num] = dic.get(num,0) + 1

    for i in sortedKeys:
        sortedDic[i] = dic[i]




    return sortedDic

print(findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 1))