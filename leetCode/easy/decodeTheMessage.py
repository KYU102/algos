
def decodeMessage(key, str):
    key = key.replace(" ","")
    abcKey = 'abcdefghijklmnopqrstuvwxyz'
    codeDict = {}
    for letter in range(26):
        codeDict[abcKey[letter]] = key[letter]

    index = 0
    davincisCode = ""
    
    while(str[index]):
        if str[index] == " ":
            davincisCode += " "
        else:
            davincisCode = davincisCode + codeDict[str[index]]
        index+=1


    return davincisCode


print(decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))