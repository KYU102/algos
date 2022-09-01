def canConstruct(ransomNote, magazine):

    ranCounter = {}
    magCounter = {}

    if len(ransomNote) > len(magazine):
        return False

    ransomNote = ransomNote.split().sort()

    return ransomNote




print(canConstruct('aasgawgheshhsa','badasgEAGESAGAHAEHSEHAESHEAHAEHA'))

    # counter = {}

    # if len(ransomNote) > len(magazine):
    #     return False

    # for letter in ransomNote:
    #     counter[letter] = counter.get(letter, 0) + 1
    
    # for letter in magazine:
    #     if letter in counter:
    #         counter[letter] -= 1
    
    # for key in counter:
    #     if counter[key] > 0:
    #         return False
    
    # return True