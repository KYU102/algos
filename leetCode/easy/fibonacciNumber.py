

def fib(n):
    seq = [0,1]

    if n == 0:
        return 0

    for i in range(n-1):
        seq.append(seq[-1] + seq[-2])
    return seq[-1]



print(fib(4))