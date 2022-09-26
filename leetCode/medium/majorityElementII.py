import collections


def majorityElement(nums):
    res = []
    count = collections.Counter(nums)
    for key, val in count.items():
        if val > len(nums)//3:
            res.append(key)

    return res

print(majorityElement([2,3]))