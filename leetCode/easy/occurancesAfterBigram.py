
def findOccurances(text, first, second):

    res = []
    text = text.split()

    for i in (range(len(text) - 2)):
        if text[i] == first and text[i + 1] == second:
            res.append(text[i+2])

    return res

print(findOccurances("alice is a good girl she is a good student","a","good"))