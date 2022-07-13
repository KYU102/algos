function addDigits (num){
    
    let newNum = num
    let subNum = 0
    
    if (num < 10){
        return num 
    }
    
    while (newNum > 10 ){
        let numsArr = Array.from(String(newNum), Number)
        for (let i = 0; i < numsArr.length; i++) {
            subNum += numsArr[i]
            
        }
        newNum = subNum
        subNum = 0
    }
    return newNum
}

console.log(addDigits(2))