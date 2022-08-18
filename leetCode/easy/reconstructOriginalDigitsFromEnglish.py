
def originalDigits(s):
    count = {}
    for letter in s:
        count[letter] = count.get(letter, 0) + 1
    
    return count

print(originalDigits("owoztneoer"))