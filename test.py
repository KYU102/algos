
from mailcap import findmatch
from string import ascii_lowercase


def findMostStacks(text):
    
    arr = text.split()
    res = []
    
    for word in arr:

        if word[len(word)-2:len(word)] == 'ly' or word[len(word)-2:len(word)] == 'ed':
            word = (word[0:len(word)-2])
        elif word[len(word)-3:len(word)] == 'ing':
            word = (word[0:len(word)-3])
        if len(word) > 8:
            word = (word[:8])
        res.append(word)

        

    return res


print(findMostStacks('an extremely dangerous dog is barking'))