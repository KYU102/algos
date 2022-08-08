
def largestOddNumber(num):

    num = int(num)
    

    while num > 0:
        if num % 2 == 0:
            num  = num//10
        else:
            return str(num)
    
    return ""
    






print(largestOddNumber("22223"))