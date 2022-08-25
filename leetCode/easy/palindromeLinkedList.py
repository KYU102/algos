def isPalindrome(head):
    arr = []

    while runner.next:
        arr.append(runner.val)
        head = head.next
    
    if arr == arr[::-1]:
        return True
    else:
        return False

