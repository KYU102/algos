
def longestPalindrome(s):

    longest = ""

    left, right = 0, 1

    while right != len(s) - 1:
        if s[left:right] != s[left:right,-1]:
            return "x"

print(longestPalindrome("babad"))