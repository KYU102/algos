def minSetSize(arr):
    count = {}
    counter = 0
    half = len(arr)//2

    for num in arr:
        count[num] = count.get(num, 0) + 1

    sorted_dict = {}
    sorted_keys = sorted(count, key=count.get, reverse=True)

    for w in sorted_keys:
        sorted_dict[w] = count[w]

    for key in count:
        counter+=1
        half -= count[key]
        if half < 1:
            break



    return len(arr) - counter

print(minSetSize([9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]))