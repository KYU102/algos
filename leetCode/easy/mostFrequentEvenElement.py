import collections

def mostFrequentEven(nums):
    nums.sort()
    count = {}
    for num in nums:
        if num%2==0:
            count[num] = count.get(num,0) + 1
    
    return max(count,key=count.get,default=-1)

print(mostFrequentEven([8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]))







    # class Solution:
    # def majorityElement(self, nums):
    #     counts = collections.Counter(nums)
    #     return max(counts.keys(), key=counts.get)