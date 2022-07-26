

def getRow(rowIndex):

    start = [[1],[1,1]]
    subArray = []

    if rowIndex == 0:
        return start[0]

    if rowIndex == 1:
        return start[1]

    rowIndex = rowIndex - 2
    
    while(rowIndex > 0):
        initiall = [1]
        rowIndex -= 1
        


print(getRow(1))