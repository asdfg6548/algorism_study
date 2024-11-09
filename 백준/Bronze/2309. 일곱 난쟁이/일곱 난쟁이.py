from itertools import combinations
arr=[]

for i in range(9):
    inp=int(input())
    arr.append(inp)

lis=list(combinations(arr,7))

for i in lis:
    if sum(i)==100:
        for j in sorted(i):
            print(j)
        break