from asyncio import tasks


def taskScheduler(tasks,space):
    taskIndex = {}
    arr = []
    res = 0
    i=0
    while i < len(tasks):
        if tasks[i] not in taskIndex:
            taskIndex[tasks[i]] = i
            res+=1
        else:
            gap = space - i - taskIndex[tasks[i]]
            if gap > 0:




    return taskIndex

print(taskScheduler([1,2,1,2,3,1],3))