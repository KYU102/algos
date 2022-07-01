def isSubsequence (str, test):
    # compareStr = ""
    # for strLetter in range(len(str)):
    #     for testLetter in range(len(test)):
    #         if str[strLetter] == test[testLetter]:
    #             compareStr += test[testLetter]
    #             test = test[testLetter+1:len(test)]
    #             break
    
    # if  compareStr == str:
    #     return True
    # else: return False
        if len(str) > len(test):return False
        if len(str) == 0:return True
        subsequence=0
        for i in range(0,len(test)):
            if subsequence <= len(str) -1:
                print(str[subsequence])
                if str[subsequence]==test[i]:

                    subsequence+=1
        return  subsequence == len(str) 



print(isSubsequence("acb", "apbbpc"))

# iterate through the str to see if the leters are there 
# splice the test string everytime there is a letter there 