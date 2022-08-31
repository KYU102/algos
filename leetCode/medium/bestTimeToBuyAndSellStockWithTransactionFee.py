def maxProfit(prices,fee):
    totalP = 0
    hold = -prices[0]

    for price in prices[1:]:
        totalP = max(totalP, hold + price - fee)
        hold = max(hold, totalP - price)

    return totalP

print(maxProfit([1,3,2,8,4,9],2))