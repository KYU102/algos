
def distributeCandies(candyType):

    count = {}

    for i in candyType:
        count[i] = count.get(i, 0) + 1

    return int(min(len(candyType)/2, len(count)))

    # built in methods
    # return int(min(len(candies) / 2, len(set(candies))))

print(distributeCandies([6,6,6,6]))