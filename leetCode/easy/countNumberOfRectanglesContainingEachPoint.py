def countRectangles(rectangles, points):
    count = 0
    res = []
    for point in points:
        for rectangle in rectangles:
            if point[0] <= rectangle[0] and point[1] <= rectangle[1]:
                count += 1
        res.append(count)
        count = 0
    
    return res


print(countRectangles([[1,2],[2,3],[2,5]],[[2,1],[1,4]]))