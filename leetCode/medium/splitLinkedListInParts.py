def splitListToParts(head, k):

    runner = head
    res = []
    subArr = []
    extra = len(head) % k
    answer = []

    while runner:
        res.append(runner.val)
    
    while extra != 0:
        for i in range(len(head) % k):
            subArr.append(res[i])
        

    
    return answer