import sys
input=sys.stdin.readline

n=int(input())

d=[0]*100001

d[1]=1
d[2]=2
d[3]=4

def dp(num):
    for i in range(4,num+1):
        d[i]=d[i-1]+d[i-2]+d[i-3]

    print(d[num])



for i in range(n):
    a=int(input())
    dp(a)
