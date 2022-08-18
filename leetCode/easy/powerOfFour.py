
def isPowerOfFour(n):

    power = 0
    while 4^power < n:
        if 4^power == n:
            return True
        power += 1
    
    return False

print(isPowerOfFour(16))


