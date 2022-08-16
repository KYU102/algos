


def isPerfectSquare(num) -> bool:
    test = 0
    testSquared = 0
    while testSquared < num:
        testSquared = test*test
        if testSquared == num:
            return True
        test+=1
    
    return False



print(isPerfectSquare(100))