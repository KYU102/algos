def canConstruct(ransomNote, magazine):

    counter = {}

    if len(ransomNote) > len(magazine):
        return False

    for letter in ransomNote:
        counter[letter] = counter.get(letter, 0) + 1
    
    for letter in magazine:
        if letter in counter:
            counter[letter] -= 1
    
    for key in counter:
        if counter[key] > 0:
            return False
    
    return True




print(canConstruct('aasgawgheshhsa','badasgEAGESAGAHAEHSEHAESHEAHAEHA'))

