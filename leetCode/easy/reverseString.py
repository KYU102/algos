
from re import S


def reverseString(s):

    left,  right = 0, len(s) - 1

    while left != right or left + 1 == right:

        s[left], s[right]= s[right],s[left]

        left +=1
        right -= 1

    return s


print(reverseString(["h","e","l","l","o"]))

        
