let num = 121

function isPalindrome (x) {
    let reversed = x.toString().split("").reverse().join("")
    if(reversed == x){
        return true
    }
    else {
        return false
    }
};

console.log(isPalindrome(num))