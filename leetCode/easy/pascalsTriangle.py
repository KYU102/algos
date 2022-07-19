def generate(numRows):
    
    output = [[1],[1,1]]

    if numRows == 1:
        return output[0]
    if numRows == 2:
        return output


    counter = 2
    while(counter != numRows):
        counter+=1
        theEnd = output[-1]
        subSection = [1]
        for i in range(1, counter - 1):
            subSection.append(theEnd[i -1] + theEnd[i])
        
        subSection.append(1)
        output.append(subSection)
        subSection = [1]
    
    return output




print(generate(6))