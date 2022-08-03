

def judgeCircle(moves):
    # this is the hard code method
    # position = [0,0]

    # for input in moves:
    #     if input == 'U':
    #         position[0] += 1
    #     if input == 'D':
    #         position[0] -= 1
    #     if input == 'R':
    #         position[1] += 1
    #     if input == 'L':
    #         position[1] -= 1

    # if position == [0,0]:
    #     return True

    # return False

    return ((moves.count('L') == moves.count('R')) and (moves.count('U') == moves.count('D')))



print(judgeCircle("UDL"))