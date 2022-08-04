
def nextGreatestLetter(letters, target):

    alfabet = "abcdefghijklmnopqrstuvwxyz"
    dict = {}   
    counter = 0

    for letter in alfabet:
        dict[letter] = counter
        counter+=1
    
    for i in letters:
        if dict[i] > dict[target]:
            return i
            
    
    return letters[0]

print(nextGreatestLetter(["c","f","j"], "a"))