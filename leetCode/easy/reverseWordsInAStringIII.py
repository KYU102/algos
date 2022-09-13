def reverseWords(s):

    res = ''
    s = s.split()
    for word in s:
        for letter in word[::-1]:
            res+=letter
        res+=' '

    res = res.rstrip()
    return res
print(reverseWords("Let's take LeetCode contest"))