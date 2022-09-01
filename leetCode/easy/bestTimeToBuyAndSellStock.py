def maxProfit(prices):
    max = 0
    left, right = 0,1

    while right < len(prices):
        if prices[left]>prices[right]:
            left = right
        if prices[right]- prices[left] > max:
            max = prices[right]- prices[left]
        right+=1
    return max

print(maxProfit([7,1,5,3,6,4]))