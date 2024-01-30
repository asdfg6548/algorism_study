N = int(input())
 
goal = [int(input().strip()) for i in range(N)]
 
ans = []  
stack = []  
num = 1 
 
for g in goal:
    while num <= g: 
        stack.append(num)
        ans.append("+")
        num += 1
 
    if stack and stack[-1] == g: 
        stack.pop()
        ans.append("-")
    else:
        print("NO")
        break
else:
    for action in ans:
        print(action)