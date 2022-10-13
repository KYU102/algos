

def longestPalindrome(s: str) -> int:
    count = {}
    longest = 1
    alleven = True
    for letter in s:
        count[letter] = count.get(letter,0) + 1

    for key in count:
        if count[key]%2 == 0:
            longest += count[key]
        else:
            longest += count[key] -1
            alleven = False
    if alleven:
        longest -= 1
    return longest


print(longestPalindrome('aa'))