def countHomogenous(s):

    dic = {}

    left, right = 0,1

    for letter in s:
        dic[letter] = dic.get(letter, 0) + 1 
    
    while left < len(s):
        if s[left] != s[right]:
            left = right
            right += 1
        else:
            dic[s[left:right]] = dic.get([s[left:right]], 0) + 1 

    
    return dic

print(countHomogenous("abbcccaa"))