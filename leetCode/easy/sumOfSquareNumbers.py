
from operator import truediv


def judgeSqr(c):

    a = 0
    b = 0

    while a^a + b^b < c:
        if a^a + b^b == c:
            return True
        
        if a >= b:
            a+=1
        else:
            b+=1
        
    return False

print(judgeSqr(10))