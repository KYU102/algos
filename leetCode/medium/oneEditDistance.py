

def isOneEditDistance(s,t):
    counter = 0
    if abs(len(t) - len(s)) > 1:
        return False

    if len(s) == 1 and len(t) == 0 or len(s) == 0 and len(t) == 1:
        return True

    if len(s) == len(t):
        for i,j in zip(s,t):
            if i != j:
                counter+=1

    l = r = 0

    if len(s) != len(t):
        if len(s) < len(t):
            counter+=1
        while r != len(t) and l != len(s):
            if s[l] == t[r]:
                l+=1
                r+=1
            else:
                if len(s) > len(t):
                    l+=1
                    counter+=1
                else:
                    r+=1
                    counter +=1

    return counter == 1


print(isOneEditDistance('ab','acb'))