<<<<<<< HEAD

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
=======
from string import ascii_lowercase


def test(message, rotation = 4):
    rotated = ascii_lowercase[rotation:] + ascii_lowercase[:rotation]
    cipher = {o: n for o, n in zip(ascii_lowercase,rotated)}

    encoded = []
    for char in message.lower():
        if char in cipher:
            encoded.append(cipher[char])
        else:
            encoded.append(char)

    return''.join(encoded)

print(test('SUPER'))
>>>>>>> 4586e655f0aaf754caf0842182eb091856bba271
