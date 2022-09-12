def longestPalindrome(s):

    count = {}
    counter = 0
    odd = False

    for letter in s:
        count[letter] = count.get(letter,0)+1
    
    for val in count.values():
        if val%2 == 0:
            counter+=val
        else:
            counter+=val-1
            odd = True
    
    if odd:
        return counter + 1
    else:
        return counter


print(longestPalindrome("abccccdd"))