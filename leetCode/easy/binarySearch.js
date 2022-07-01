var num = [-1,0,3,5,9,12]
var targe = 9

function search (nums, target){
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === target){
            return i 
        }
        
    }
}

console.log(search(num, targe))