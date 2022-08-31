


def maxProfit(prices):
    max = 0
    l, r = 0,1

    while r < len(prices):
        if prices[l] > prices[r]:
            l = r
        if prices[r] > prices[l]:
            max += prices[r] - prices[l]
            l=r
        r+=1

    return max


print(maxProfit([7,6,4,3,1]))