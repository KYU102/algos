/** ked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
function reverseList(head) {
    let prev = null
    let current = head
    let next = null

    if(this.head === null)
        return "list is empty"

    if (this.head.next === null){
        return {ListNode}
    } 

    while(this.head){
        next = current.next
        current.next = prev
        prev = head
        head = next
    }
};