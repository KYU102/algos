

def letterCombiantions(digits):
        numDict = {'2': "abc",
                '3': "def",
                '4': "ghi",
                '5': "jkl",
                '6': "mno",
                '7': "pqrs",
                '8': "tuv",
                '9': "wxyz"
        }

        lettersNeeded = []

        possibleCombos = []


        for num in digits:
                possibleCombos = numDict[num]

        return possibleCombos


print(letterCombiantions("234"))