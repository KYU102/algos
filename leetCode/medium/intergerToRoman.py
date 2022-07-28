
def intToRoman (str):
    
    numDiction = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500, 'M':1000}

    number = 0

    for i in str:
        number += numDiction[i]
        if numDiction[i]<numDiction[i+1]:
            number -= numDiction[i] * 2

    return number


print(intToRoman("LV"))

