
def decodeMessage(key, str):
    key.replace(" ","")
    abcKey = 'abcdefghijklmnopqrstuvwxyz'
    codeDict = {}
    for letter in range(len(key)):
        if key[letter] not in codeDict:
            codeDict[abcKey[letter]] = key[letter]


    davincisCode = ""
    
    for index in range(len(str)):
        if str[index] == " ":
            davincisCode += " "
        else:
            davincisCode += codeDict[str[index]]


    return davincisCode


print(decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))