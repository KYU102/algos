
def largestOddNumber(num):

    for i in range(len(num)):
        print(i)
        if int(num[i]) % 2 == 1:
            print(i)
            return num[:i]
        
    return num[:2]

print(largestOddNumber("35427"))