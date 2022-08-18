def minSetSize(arr):
    count = {}

    for num in arr:
        count[num] = count.get(num, 0) + 1

    sorted_dict = {}
    sorted_keys = sorted(count, key=count.get)

    for w in sorted_keys:
        sorted_dict[w] = count[w]

    return sorted_dict

print(minSetSize([3,3,3,3,2,2,7,5,5,5]))