

def findAndReplacePattern(words, pattern):
    decoder= {}
    compDic = {}
    counter = 1
    indexer = 1
    answer = []

    while indexer != len(pattern) + 1:

        indexer += 1

        if decoder[indexer] != decoder[indexer-1]:
            decoder[indexer] 

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

print(findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb"))