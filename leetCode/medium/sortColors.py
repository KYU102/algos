def sortColors(nums):

    counter = {}
    result = []

    for color in nums:
        counter[color] = counter.get(color, 0) + 1

    for num in range(3):
        for counts in range(counter[num]):
            result.append(num)

    return result



print(sortColors([2,0,2,1,1,0]))
