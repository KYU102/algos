def reverse(x):
    res = str(x)

    if x < 0:
        res = int(res[len(res):0:-1]) * -1
    else:
        res = int(res[len(res)::-1])
    
    if res > 2**31 or res < -2**31:
        return 0
    else:
        return res
    




print(reverse(123))