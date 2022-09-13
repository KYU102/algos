def maxProfit(prices):
    maxP = 0
    left, right = 0,1

    while right < len(prices):
        if prices[left]>prices[right]:
            left = right
        maxP = max(maxP, prices[right]- prices[left])
        right+=1
    return maxP

print(maxProfit([7,1,5,3,6,4]))