

function convert ( str, numRows){
    let repeatStr = str
    let newStr = ""
    for( let i = 0; i < numRows; i++){
        repeatStr += str
    }
    
    for(let j = 0; j < numRows; j++){
        newStr += repeatStr[j+numRows+2]
    }
    console.log(newStr)
}

convert("PAYPALISHIRING", 3)