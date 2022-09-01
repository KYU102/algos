def firstBadVersion(n):
    for i in range(n):
        if not isBadVersion(i):
            return i+1

    