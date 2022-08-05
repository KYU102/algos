
def calPoints(ops):

    score = []

    for points in ops:
        if points == 'C':
            score.pop()
        elif points == 'D':
            score.append(int(score[-1])*2) 
        elif points == '+':
            score.append(int(score[-1]) + int(score[-2]))
        else:
            score.append(int(points))

    return sum(score)

print(calPoints(["5","-2","4","C","D","9","+","+"]))