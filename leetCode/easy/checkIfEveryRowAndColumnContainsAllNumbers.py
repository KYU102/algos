def checkValid(matrix):
    counter = {}

    for i in matrix:
        for j in i:
            counter[j] = counter.get(j, 0 ) + 1

    for key in counter:
        if counter[key] != len(matrix):
            return False

    return True

print(checkValid([[1,2,3],[3,1,2],[2,3,1]]))