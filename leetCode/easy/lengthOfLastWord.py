def lengthOfLastWord(str):
    counter = 1
    index = len(str) -1
    while (str[index] != " " and index > 0):
        counter += 1 
        index -= 1
        if str[index - 1] == " ":
            counter -= 1
    
    return counter




print(lengthOfLastWord("hello world"))

