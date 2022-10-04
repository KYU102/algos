# 2 palyers are given a string
# one player can have substrings that start with 
# a vowel and other a consonant
# the player that can make the most substrings wins 
# duplicates count for each individual occurance
def minionGameWinner(s):
    
    vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']
    Stuart = 0
    Kevin = 0
    index = 0

    while index < len(s):
        if s[index] not in vowels:
            Stuart += len(s) - index
        else:
            Kevin += len(s) - index

        index+=1
    
    if Kevin == Stuart:
        return 'Draw'
    if Stuart > Kevin:
        return 'Stuart {}'.format(Stuart)
    else:
        return 'Kevin {}'.format(Kevin)

    


print(minionGameWinner('BANAASA'))


