
def divide(dividend, divisor):
    count = 0
    sum = 0
    temp = 0

    
    if divisor < 0:
        temp =  divisor * -1
        while sum < dividend:
            sum += temp
            count+=1
        if sum > dividend and divisor < 0:
            count -=1
        return count * -1

    while sum < dividend:
        sum += divisor
        count+=1
    
    if sum > dividend and divisor > 0:
        count -=1
        return count
    

    return count

print(divide(7,-3))