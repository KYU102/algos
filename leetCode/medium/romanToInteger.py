
def romanToInt (str):

    #created a dictionary to hold all of the values
    numDiction = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500, 'M':1000}
    answer = 0

    # "list()" turns each letter of the string into an array
    letterList = list(str)

    # edge case: if it is a single letter then return the value of that letter
    if len(str) == 1:
        return numDiction[letterList[0]]

    # iterate through the array and add each letter to the total
    for letter in letterList:
        answer += numDiction[letter]

    # iterate through each letter of the array
    for i in range(len(letterList) - 1):

        # if the number after i is less than the number after it
        # then remove 2x of the value of i to compensate
        # adding it 
        if(numDiction[letterList[i]]<numDiction[letterList[i+1]]):
            answer -= 2*(numDiction[letterList[i]])
    return answer

        

print(romanToInt("DI"))