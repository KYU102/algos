// Given an array of integers nums and an integer target, 
// return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, 
// and you may not use the same element twice.

// You can return the answer in any order.

var nums1 = [2,7,11,15]
var target1 = 9

var nums2 = [3,2,4]
var target2 = 6

var nums3 = [2,5,5,11]
var target3 = 10

function twoSum(nums, target){
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] + nums[j] === target){
                return [i,j]
            }
        }
        
    }
}

console.log(twoSum(nums1, target1))
console.log(twoSum(nums2, target2))
console.log(twoSum(nums3, target3))