def checkRecprd (s):
    
    absentCount = 0
    for i in range(len(s)):
        if (s[i] == 'A'):
            absentCount += 1
        if (absentCount == 2):
            return False
        if(i < len(s) - 3):
            if (s[i] == 'L' and s[i + 1] == 'L' and s[i + 2] == 'L' ):
                return False
    
    return True


print(checkRecprd("PPALLL"))