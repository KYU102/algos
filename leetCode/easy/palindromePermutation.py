
def canPermutePalidrome(s):

    dic = {}
    numOfOdd = 0

    for i in s:
        dic[i] = dic.get(i, 0) + 1

    for key in dic:
        if dic[key] % 2 == 1:
            numOfOdd += 1

    if len(s) % 2 == 0 and numOfOdd == 0:
        return True
    if len(s) % 2 == 1 and numOfOdd == 1:
        return True

    return False


print(canPermutePalidrome("aabaa"))