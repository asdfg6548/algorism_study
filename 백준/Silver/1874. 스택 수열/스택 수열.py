import sys
n = int(sys.stdin.readline())
stack = []
result = []
is_valid = True
cnt = 1
for _ in range(n):
    target = int(sys.stdin.readline())
    while cnt <= target:
        stack.append(cnt)
        result.append("+")
        cnt += 1
    if stack[-1] == target:
        stack.pop()
        result.append("-")
    else:
        is_valid = False
        break
if not is_valid:
    print("NO")
else:
    print(*result, sep="\n")