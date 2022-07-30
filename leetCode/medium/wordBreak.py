
def wordBreak(s, wordDict):

    dict = {}
    left = 0
    right = 1

    # create counter with all words starting at 0
    for word in wordDict:
        dict[word] = 0


    while (right != len(s) + 1):
        if s[left:right] not in  dict.keys():
            right += 1
        else:
            dict[s[left:right]] +=1
            left = right
            right += 1
    
    if 0 in dict.values():
        return False

    return True

print(wordBreak("catsandog", ["cats","dog","sand","and","cat"]))