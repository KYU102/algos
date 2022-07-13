function isPowerOfThree(num){
    numSqr = num / 3
    if (num === 0){
        return false
    }
    if (numSqr % 3 ===0){
        return true
    }
    else{
        return false
    } 
    
}