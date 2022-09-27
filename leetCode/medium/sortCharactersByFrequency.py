
from audioop import reverse
from typing import Counter


def frequencySort (s):
    counter = {}
    res=''
    for letter in s:
        if letter not in counter:
            counter[letter] = counter.get(letter, 1)
        else:
            counter[letter] += 1

    sortedCounter = sorted(counter,key=counter.get,reverse=True)


    for letter in sortedCounter:
        res+=letter*counter[letter]




    return res


print(frequencySort("tree"))