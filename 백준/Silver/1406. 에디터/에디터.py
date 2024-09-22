import sys
input = sys.stdin.readline

left=list(input().rstrip())
right=[]

n=int(input())

for i in range(n):
    command=list(input().split())
    if command[0]=='L' and left:
        right.append(left.pop())
    elif command[0]=='D'and right:
        left.append(right.pop())
    elif command[0]=='B' and left:
        left.pop()
    elif command[0] == 'P':
        left.append(command[1])

res=left+right[::-1]
print(''.join(res))