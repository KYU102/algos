def checkPowerOfThree(n):

    powers = [1]
    power = 1

    while 3*power <= n:
        powers.append(3*power)
        power +=1

    return powers

print(checkPowerOfThree(100))