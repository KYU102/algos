from collections import Counter

def findAndReplace(words, pattern):
    decoder= {}
    compDic = {}
    counter = 1
    indexer = 1
    answer = []

<<<<<<< HEAD:leetCode/medium/findAndReplace.py

    for i in range(len(pattern)):
        if pattern[i] != pattern[i-1]:
            decoder[i] = counter
            counter = 1
        else:
            counter += 1 
            decoder[i] = counter


        

    
        
=======
    while indexer != len(pattern) + 1:
        print(indexer)
        indexer += 1
    
>>>>>>> a1c021b3d51b95b637cf9d52ff421d7bade6b438:leetCode/medium/findAndReplacePattern.py
    # print (decoder)
    # counter = 0
    # for word in words:
    #     for letter in range(1, len(word)):
    #         counter +=1
    #         if word[letter] != word[letter - 1]:
    #             compDic[letter] = counter
    #             counter = 1
    #         if decoder == compDic:
    #             answer.append(word)
    #     print(compDic)
    #     compDic = {}
        

    return decoder

print(findAndReplace(["abc","deq","mee","aqq","dkd","ccc"], "abb"))