
def firstUnique(s):
    dic = {}

    for letter in s:
        dic[letter] = dic.get(letter, 0) + 1

    for key in dic:
        if dic[key] == 1:
            return s.index(key)

    return -1

print(firstUnique('leetcode'))