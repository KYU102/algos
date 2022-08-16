
from unicodedata import name


def maxProfit(prices):
    
    max = 0
    profit = 0
    left = 0
    right = 1
    
    while right != len(prices) - 1 and left != len(prices) - 2:
        if prices[left] > prices[left + 1]:
            left+=1
        if profit > max:
            max = profit
        



    return nArray

print(maxProfit([7,1,5,3,6,4]))