def backSpaceCompare(s,t):

    sArr = []
    tArr = []

    for letter in s:
        if letter == '#' and len(sArr) > 0:
            sArr.pop()
        if letter != '#':
            sArr.append(letter)
    
    for letter in t:
        if letter == '#' and len(tArr) > 0:
            tArr.pop()
        if letter != '#':
            tArr.append(letter)


    return sArr == tArr

print(backSpaceCompare("ab##","c#d#"))