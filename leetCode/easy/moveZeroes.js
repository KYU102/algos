

function moveZeroes(nums){
    let zeroCounter = 0
    for (let i = 0; i < nums.length; i++) {
        if(nums[i] === 0){
            zeroCounter++
            nums.splice(i,1)
            i--
        }
    }
    while ( zeroCounter > 0){
        nums.push(0)
        zeroCounter--
    }
    return nums
}

console.log(moveZeroes([1,0,1,0,0,0,1,1,1,1]))