def lastStoneWeight(stones):

    stones.sort()
    while len(stones) > 1:
        stones[-2] = stones[-1] - stones[-2]
        stones.pop()
        stones.sort()
    return stones[0]

print(lastStoneWeight([2,7,4,1,8,1]))