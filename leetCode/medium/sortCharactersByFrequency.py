
from typing import Counter


def frequencySort (s):
    counter = {}
    sortedCounter = counter.items()
    for letter in s:
        if letter not in counter:
            counter[letter] = counter.get(letter, 1)
        else:
            counter[letter] += 1



    return sortedCounter


print(frequencySort("tree"))