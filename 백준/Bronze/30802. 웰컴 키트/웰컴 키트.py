import sys
input = sys.stdin.readline


n=int(input())
arr=list(map(int,input().split()))
t,p=map(int,input().split())
res1=0

for i in arr:
    if i == 0:
        continue  # 0인 경우 티셔츠 필요 없음
    res1 += (i + t - 1) // t  # 올림 처리

res2=n//p
res3=n%p

print(res1)
print(res2,res3)