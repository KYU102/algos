def tribonacci(n):
    seq = [0,1,1]

    if n == 0:
        return 0
    if n < 3:
        return 1

    for i in range(n-2):
        seq.append(seq[-1]+seq[-2]+seq[-3])

    return seq[-1]

print(tribonacci(3))