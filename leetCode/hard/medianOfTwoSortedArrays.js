nums1 = [3, 2, 4, 5]
nums2 = [-2,-1]

function findMedianSortedArrays(nums1, nums2) {
    let median = 0
    let sortedNums = nums1.concat(nums2).sort()
    console.log(sortedNums)
    if(sortedNums.length % 2 === 1){
        median = sortedNums [Math.floor(sortedNums.length/2)]
    }
    else {
        median = ((sortedNums[sortedNums.length/2]) + (sortedNums[sortedNums.length/2 - 1])) / 2
    }
    return median
};

console.log(findMedianSortedArrays(nums1, nums2))