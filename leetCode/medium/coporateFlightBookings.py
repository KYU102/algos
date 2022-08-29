def corpFlightBookings(bookings, n):
    res = []

    for i in range(n):
        res.append(0)

    for booking in bookings:
        print(booking)
        for i in range(booking[0]-1, booking[1]):
            res[i]+=booking[2]

    return res

print(corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]], 5))