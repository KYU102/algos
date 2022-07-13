function searchInsert ( nums, target) {
    let halfway = nums.length / 2 

    if (nums[0] === target){
        return 0 
    }
    if (nums[nums.length - 1] === target){
        return nums.length - 1 
    }

    while (nums[halfway] != target){
        if (nums[halfway] < target){
            halfway = Math.floor(halfway/2)
        }
        if (nums[halfway] > target){
            halfway = Math.floor(halfway * 1.5)
        }
        if (halfway === 0){
            return nums.length
        }
    }

    return halfway
}
console.log(searchInsert([1,3,5,6],0))

for (let index = 0; index < nums.length; index++) {
    if (nums[index] === target){
        return index
    }
    if (nums[index] > target){
        return index
    }
    
}
return nums.length