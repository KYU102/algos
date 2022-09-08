def countSubstrings(s):
    
    counter = len(s)

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[j:i:-1]:
                counter += 1
    return counter

print(countSubstrings("aaa"))