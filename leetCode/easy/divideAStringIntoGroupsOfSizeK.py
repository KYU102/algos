

def divideString(s, k, fill):

    array = []

    if k >= len(s):
        return [s + fill*(k-len(s))]

    if len(s)%k != 0:
        s += (fill *(k - len(s)%k))
    
    for subS in range(0,len(s),k):
        array.append(s[subS:subS+k])
        
    return array



print(divideString("asfgaFASGAFASGss", 40,'X'))