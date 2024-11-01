n,m=map(int,input().split())

arr=[]

for i in range(n):
    a=int(input())
    arr.append(a)
arr.sort()

res=2000000001
front=0
back=0

while front <= back < n:
    if arr[back]-arr[front]<m:
        back+=1

    else:
        res=min(res,arr[back]-arr[front])
        front+=1

print(res)