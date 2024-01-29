n = int(input())
res = []

for i in range(n):
    a = int(input())
    if a == 0:
        res.pop()
    else:
        res.append(a)

print(sum(res))
