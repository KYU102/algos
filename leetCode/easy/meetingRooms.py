
def canAttendMeeting(intervals):
    intervals.sort()

    for slot in range(len(intervals)-1):
        if intervals[slot][1] > intervals[slot + 1][0]:
            return False
    
    return True




print(canAttendMeeting([[7,10],[2,8]]))