from re import L


def numOfWeakCharacters(properties):

    if len(properties) == 1:
        return 0

    properties.sort(reverse=True)
    counter = 0
    for i in range(len(properties)-1):
        for j in range(i+1,len(properties)):
            if properties[i][1] > properties[j][1] and properties[i][0] > properties[j][0]:
                counter += 1
    return counter


print(numOfWeakCharacters([[2,2],[3,3]]))