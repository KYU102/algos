


def findMedianSortedArrays(nums1, nums2) :
    median = 0
    nums = (nums1 + nums2).sort()
    return nums2

    if len(nums) == 0:
        return "this list is empty"

    if len(nums) % 2 == 0:
        median = nums[0] +  nums[1]
        return median
    
    else:
        return nums[len(nums)/2]



print(findMedianSortedArrays([1,2], [3,4,5]))
