
def removeKDigits(num, k):

    if k == len(num):
        return '0'

    left = 0
    right = left + k

    largest = 0
    index = []
    
    while right != len(num) - 1:
        if int(num[left:right]) > largest:
            largest = int(num[left:right])
            index = [left, right]
        left+=1



    return num.replace(num[index[0]:index[1]],'')

print(removeKDigits('431513', 2))