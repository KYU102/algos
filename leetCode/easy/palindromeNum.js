let num = 12132456

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