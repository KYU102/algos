
class Solution:
    def twoSum(nums, target):
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i

# here we are building a hashmap of the values and the indexes, while checking if
# the difference in target and if the current number sums up to the target

    print(twoSum([3,2,4],6))