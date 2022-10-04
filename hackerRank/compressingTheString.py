from itertools import groupby

s= input()
print(*[(len(list(j)),int(i))  for i, j in groupby(s)])