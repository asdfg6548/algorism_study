import sys
input = sys.stdin.readline

n=int(input())

for i in range(n):
    a,b=map(str,input().split())
    first = list(a)
    second = list(b)
    #정렬
    first.sort()
    second.sort()
    # 글자수부터 비교
    if len(first)!=len(second):
        print("Impossible")
    elif first!=second:
        print("Impossible")
    else:
        print("Possible")