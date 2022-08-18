def isPowerOfThree(n):

    power = 1
    
    while power <= n:
        if power == n:
            return True
        power*=3
    
    return False

print(isPowerOfThree(27))

