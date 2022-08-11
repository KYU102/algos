def kthDistinct(arr, k):

    dic = {}
    timesFound = 0

    for i in arr:
        dic[i] = dic.get(i, 0) + 1

    for key in dic:
        if dic[key] == 1:
            timesFound +=1

        if timesFound == k:
            return key
    
    return ""

print(kthDistinct(["d","b","c","b","c","a"],2))