
def heightChecker(heights):
    counter = 0
    sortedH = sorted(heights)

    for i in range(len(heights)):
        if sortedH[i] != heights[i]:
            counter += 1

    return counter

print(heightChecker([1,1,4,2,1,3]))