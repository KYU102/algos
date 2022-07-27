

def searchMatrix(matrix, target):
    
    # left = matrix[0][0]
    # right = matrix[len(matrix) - 1][-1]

    # if left == target: return True
    # if right == target: return True

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return True

    return False




print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 11))