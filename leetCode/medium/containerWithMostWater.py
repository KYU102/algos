

def maxArea(height):
    # Brute force method:
    # max = 0
    # area = 0

    # for left in range(len(height)):
    #     for right in range(left + 1, len(height)):
    #         if height[left] > height[right]:
    #             area = height[right] * (right - left)
    #         if height[right] > height[left]:
    #             area = height[left] * (right - left)
    #         if height[left] == height[right]:
    #             area = height[left] * (right - left)
    #         if area > max:
    #             max = area
    
    # return max

    # Greedy method:

    left, right, maxArea = 0, len(height) - 1 , 0

    while right > left:
        maxArea = max(maxArea, (right - left) * min(height[left], height[right]))
        # ^ the max area is calculated by the lower of the 2 heights "min()" and then
        # miltiplied by the difference of left/right indexes. if that area is higher tha
        # the max then set it as the max
        if left > right:
            right -= 1
        else:
            left += 1
        # ^ the if else statemtn is greedily useing the larger height as the starting point

    return maxArea




print(maxArea([1,8,6,2,5,4,8,3,7]))