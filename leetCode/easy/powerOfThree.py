def isPowerOfThree(n):

    power = 0
    
    if n == 1: return True
    if n < 3: return False
    while 3**power <= n:
        if 3**power == n:
            return True
        power+=1
    
    return False

print(isPowerOfThree(0))

