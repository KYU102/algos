
def wordPattern(pattern, s):

    dict = {}
    abc = []
    array = s.split()

    for letter in range(len(pattern)):
        if pattern[letter] not in dict:
            dict[pattern[letter]] = array[letter]
        if dict[pattern[letter]] != array[letter]:
            return False

    for keys in dict:
        abc.append(keys)
    
    return abs
print(wordPattern('abba', 'dog cat cat dog'))