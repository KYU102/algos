

def plusOne(digits):

    index = len(digits) - 1

    if digits[len(digits) - 1] == 9 and len(digits) == 1 :
        digits.append(0)
        digits[0] -= 8
        return digits
    
    if digits[len(digits) - 1] < 9:
        digits[len(digits) - 1] += 1
        return digits

    while index > 0:
        if digits[index] == 9:
            digits[index] -= 9
        if digits[index -1 ] < 9:
            digits[index - 1] += 1
            return digits

        index -= 1
    
    digits[0] -= 8
    digits.append(0)
    
    return digits







print(plusOne([9,9,9]))




