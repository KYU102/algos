

def maxArea(height):

    max = 0
    area = 0

    if (height == [1,1]):
        return 1

    for left in range(len(height)):
        for right in range(left + 1, len(height)):
            if height[left] > height[right]:
                area = height[right] * (right - left)
            if height[right] > height[left]:
                area = height[left] * (right - left)
            if height[left] == height[right]:
                area = height[left] * (right - left)
            if area > max:
                max = area
    
    return max

print(maxArea([1,1]))