from itertools import combinations

def letterCombiantions(digits):
        letters = {
                '2': "abc",
                '3': "def",
                '4': "ghi",
                '5': "jkl",
                '6': "mno",
                '7': "pqrs",
                '8': "tuv",
                '9': "wxyz"
                }
        
        res = []

        def backTrack(i, curStr):
                if len(curStr) == len(digits):
                        res.append(curStr)
                        return

                for char in letters[digits[i]]:
                        backTrack(i+1, curStr + char)
                
        if digits:
                backTrack(0,'')

        return res

print(letterCombiantions("234"))