def diagonalSum(mat):
    left, right, depth = 0, len(mat[0])-1, 0
    counter = 0

    if len(mat) == 1:
        return mat[0][0]

    while right > -1:
        counter += mat[depth][left]
        counter += mat[depth][right]
        left+=1
        right -=1
        depth += 1
        if left == right:
            counter -= mat[depth][left]

    return counter


print(diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))