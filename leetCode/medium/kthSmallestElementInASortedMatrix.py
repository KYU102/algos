
def kthSmallest(matrix,k):
    superMatrix = []
    
    for subArray in matrix:
        superMatrix += subArray
    

    superMatrix.sort()
    return superMatrix[k - 1]

print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))
