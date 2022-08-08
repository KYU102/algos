

def isIsomorphic(s, t): 
    sDict = {}
    tDict = {}

    if len(s) != len(t):
        return False

    for i in s:
        sDict[i] = sDict.get(i,0) + 1
        

    for j in t:
        tDict[j] = tDict.get(j,0) + 1
    
    return tDict


print(isIsomorphic('egg', 'add'))