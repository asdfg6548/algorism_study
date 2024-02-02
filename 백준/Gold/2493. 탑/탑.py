import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
stack = [(data[0], 1)]
res = [0 for i in range(n)]

for i in range(1, n):
    if data[i] < stack[-1][0]:
        res[i] = stack[-1][1]
        stack.append((data[i], i + 1))
    else:
        while True:
            stack.pop()
            if len(stack) == 0:
                stack.append((data[i], i + 1))
                break
            if data[i] < stack[-1][0]:
                res[i] = stack[-1][1]
                stack.append((data[i], i + 1))
                break


print(*res)
