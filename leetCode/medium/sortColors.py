def sortColors(nums):

    counter = {}
    result = []

    for color in nums:
        counter[color] = counter.get(color, 0) + 1

    for i in range(counter[0]):
        result.append(0)
    for i in range(counter[1]):
        result.append(1)
    for i in range(counter[2]):
        result.append(2)
    return result

print(sortColors([2,0,2,1,1,0]))
