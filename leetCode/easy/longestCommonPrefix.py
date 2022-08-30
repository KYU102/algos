def longestCommonPrefix(strs):

    
    if strs == [""]:
        return ""
    
    if len(strs) == 1:
        return strs

    compare = min(strs, key=len)
    res = ""

    index = 0
    while index < len(compare):
        for word in strs:
            if word[index] != compare[index]:
                return res
        res += compare[index]
        index += 1



print(longestCommonPrefix(["a"]))