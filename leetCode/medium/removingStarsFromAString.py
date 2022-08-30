def removeStars(s):

    res = []
    for letter in s:
        if letter == '*':
            res.pop()
        else:
            res.append(letter)

    return ''.join(res)
