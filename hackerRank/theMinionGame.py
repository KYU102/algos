# 2 palyers are given a string
# one player can have substrings that start with 
# a vowel and other a consonant
# the player that can make the most substrings wins 
# duplicates count for each individual occurance
def minionGameWinner(s):
    
    vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']
    p1 = 0
    p2 = 0
    index = 0

    while index < len(s):
        if s[index] not in vowels:
            p1 += len(s) - index
        else:
            p2 += len(s) - index

        index+=1
        
    return p2

print(minionGameWinner('banana'))


