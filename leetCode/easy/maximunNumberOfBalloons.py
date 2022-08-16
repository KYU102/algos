
def maxOfBalloons(text):
    if len(text) < 7:
        return 0

    dic = {}

    for i in text:
        dic[i] = dic.get(i, 0)+1

    return dic

print(maxOfBalloons("loonbalxballpoon"))