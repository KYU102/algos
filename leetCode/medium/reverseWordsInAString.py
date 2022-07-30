
def reverseWords(str):
    revStr = ""
    array = str.split()
    index = - 1
    while (index != (len(array) +1)*-1):
        revStr += array[index] + ' '
        index -= 1
    # for word in str.split():
    #     revStr += word + ' '
    
    return revStr[:len(str)]

print(reverseWords("blue is sky the"))
