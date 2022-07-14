
from tabnanny import check


def checkRecord (n):
    if (n == 2 ):
        return 8
    new = n -1
    totalPermutations = pow(3, n)
    late = n -2 
    absentPermutations = new*(new+1)/2 
    
    totalRecords = totalPermutations - absentPermutations -  late
    return int(totalRecords)


print(checkRecord(2))