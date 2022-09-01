

def isIsomorphic(s, t): 
    sDict = {}
    tDict = {}

    for i, j in zip(s,t):
        if i not in sDict and j not in tDict:
            sDict[i] = j
            tDict[j] = i

        elif sDict.get(i) != j or tDict.get(j) != i:
            return False

    return True




print(isIsomorphic('egg', 'add'))