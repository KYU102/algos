def findAnagrams(s,p):

    less = ''
    more = ''
    res = []

    if len(s) > len(p):
        more = s
        less = p
    else:
        more = p
        less = s
    
    for i in range(len(more)-len(less) + 1):
        print(''.join(sorted(more[i:i+len(less)])))
        if less[0] in more[i:i+len(more)]:
            if ''.join(sorted(less)) == ''.join(sorted(more[i:i+len(less)])):
                res.append(i)
    
    return res



print(findAnagrams("aaaaaaaaaaa", "aaaaaaa"))