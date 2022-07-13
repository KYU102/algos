def checkRecprd (s):
    
    recordDiction = {
        'A':'absent',
        'L':'late',
        'P':'present'
    }
    absentCount = 0
    for i in range(len(s)):
        if (s[i] == 'A'):
            absentCount += 1
        if (absentCount == 2):
            return False
        if (s[i] == 'L' & s[i + 1] == 'L' & s[i + 2] == 'L' ):
            return False
    
    return True


print(checkRecprd("PPALLL"))