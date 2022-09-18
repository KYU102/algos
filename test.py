def validSubString(pattern, str):

    vowels = ['a','e','i','o','u','y']
    count = 0

    for i in range(len(str) - len(pattern) +1 ):
        if str[i] in vowels:
            print('sucess',str[i])
        for code, letter in zip(pattern, str[i:i+len(pattern)]):
            if code == '0' and letter not in vowels:
                break
            if code == '1' and letter in vowels:
                break
            count+=1

    return count


print(validSubString('010', 'amazing'))