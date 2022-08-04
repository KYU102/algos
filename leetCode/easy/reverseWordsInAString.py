
def reverseWords(s):
    revStr = ''
    s = s.split()

    for i in s:
        revStr += i[::-1] + ' '

    
    return revStr.rstrip()

print(reverseWords("God Ding"))