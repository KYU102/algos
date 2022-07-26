

def searchRange(nums, target):
    left, right = 0, len(nums) - 1

    # first pointer that runs left until it finds the target, and it will increment 
    while nums[left] != target:
        left += 1
        if left == len(nums):
            left = -1
            break

    while nums[right] != target:
        right -= 1
        if right == 0 :
            right = -1
            break
    
    return [left, right]



print(searchRange([1,5,7,7,8,8,8,10], 10))