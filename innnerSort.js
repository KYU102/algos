/* 
  Efficiently combine two already sorted multiset arrays 
  into an array containing the sorted set intersection of the two.
  Output: only the shared values between the two arrays (deduped).
  Venn Diagram Visualization (bottom) https://i.ytimg.com/vi/sdflTUW6gHo/maxresdefault.jpg
*/

const numsA1 = [0, 1, 2, 2, 2, 7];
const numsB1 = [2, 2, 6, 6, 7];
const expected1 = [2, 7];

const numsA2 = [0, 1, 2, 2, 2, 7];
const numsB2 = [2, 2];
const expected2 = [2];

const numsA3 = [0, 1, 2, 2, 2, 7];
const numsB3 = [10];
const expected3 = [];

/**
 * Efficiently combine the two sorted arrays into a new array that is the a
 * sorted set intersection.
 * Venn Diagram Visualization (bottom):
 * @see https://i.ytimg.com/vi/sdflTUW6gHo/maxresdefault.jpg
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedA
 * @param {Array<number>} sortedB Both sets are multisets
 *    (multi in that it can contain multiple dupes).
 * @returns {Array<number>} The sorted set intersection: a new array that is
 *    sorted and contains only the shared values between the two arrays
 *    deduped.
 */
function orderedIntersection(sortedA, sortedB) {
    // CREATE A NEW ARRAY TO PUSH THE intersectionValues into
    let newArr = []
    let count = 0
    let indexA = 0
    let indexB = 0

    while (indexA < sortedA.length && indexB < sortedB.length){
        if (sortedA[indexA] === sortedB[indexB]) {
            newArr.push(sortedA[indexA])
            indexA++
            indexB++
        }
        else {
            indexA++
            
        }
    }
    
    // for( let i = 0; i < sortedA.length; i++){

    //     if (sortedA[i] !== sortedA[i + 1] ) {
    //         newArr.push(sortedA[i])
    //         count++
    //     }
    //     // else if(sortedA[i] === newArr[count]){
    //     //     continue
    //     // }
        
    //     }
    return newArr
}
console.log(orderedIntersection(numsA1, numsB1))