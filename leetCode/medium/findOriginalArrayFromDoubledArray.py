def findOriginalArray(changed):

    if len(changed) % 2 ==1:
        return []

    count = {}

    for num in range(len(changed)):
        count[num] = count.get(num,0) + 1
        
    return count

print(findOriginalArray([1,3,4,2,6,8]))