// You are given two non-empty linked lists representing 
// two non-negative integers. The digits are stored in reverse 
// order, and each of their nodes contains a single digit. 
// Add the two numbers and return the sum as a linked list.

// You may assume the two numbers do not contain any leading zero, 
// except the number 0 itself.

var l1 = [9,9,9,9,9,9,9]
var l2 = [9,9,9,9]

function addTwo ( arr1, arr2){
    let output = []
    let reversed1 = arr1.reverse()
    let reversed2 = arr2.reverse()

    if (arr1.length > arr2.length || arr1.length === arr2.length){
        for (let i = 0; i < l2.length; i++) {
            var sum = reversed1[i] + reversed2[i]
                if(sum <10 ){
                    output.push(sum)
                }
                if(sum > 9){
                    output.push(sum - 10)
                    reversed1[i+1]++
                }
                
        }
        // for(j = reversed2.length - 1; j < reversed1.lenth; j++ ){
        //     var sumExtra = reversed1[reversed2.length - 1] + reversed2[reversed2.length - 1]
        //     if(sum <10 ){
        //         output.push(sumExtra)
        //     }
        //     if(sum > 9){
        //         output.push(sumExtra - 10)
        //         reversed1[j+1]++
        //     }
        // }
        }
    return output
}

console.log(addTwo(l1, l2))