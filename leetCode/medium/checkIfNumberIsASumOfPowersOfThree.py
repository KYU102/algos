import itertools


def checkPowerOfThree(n):

    powers = []
    power = 0
    if n ==1:
        return True
    while 3**power <= n:
        powers.append(3**power)
        power +=1

    for i in range(len(powers)):
        for j in itertools.combinations(powers, i):
            print(j)
            if sum(j) == n:
                return True

    return False

    

print(checkPowerOfThree(100))