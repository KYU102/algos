
def repeatedChar(s):
    dict={}
    for letter in s:
        if letter in dict:
            return letter
        else:
            dict[letter] = 1


print(repeatedChar("abccbaacz"))

    