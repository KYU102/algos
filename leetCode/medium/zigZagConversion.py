

def convert(str, numRows):

    zagArray = []
    traverse = 'up'
    zagIndex = numRows - 1
    result = []
    answer = ""

    if len(str) == 1 or len(str) <= numRows or numRows ==1:
        return str

    for i in range(min(numRows, len(str))):
        zagArray.append([str[i]])


    for index in range(numRows, len(str)):
        if zagIndex == 0:
            traverse = 'down'
        if zagIndex == numRows - 1:
            traverse = 'up'
        
        if traverse == 'up':
            zagIndex -= 1
            zagArray[zagIndex].append(str[index])
        
        if traverse == 'down':
            zagIndex += 1
            zagArray[zagIndex].append(str[index])

    for rows in zagArray: 
        result = result + rows

    for letter in result:
        answer += letter

        
    return answer

print(convert("PAYPALISHIRING",3))

