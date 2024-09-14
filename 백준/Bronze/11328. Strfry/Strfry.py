import sys
input = sys.stdin.readline

n=int(input())

for i in range(n):
    a, b = map(str, input().split())
    # 각각 배열에 넣음
    first=list(a)
    second=list(b)
    # 정렬
    first.sort()
    second.sort()
    # 길이 비교 먼저
    if len(first) != len(second):
        print("Impossible")
        continue
    # 문자 비교
    for i in range(len(first)):
        if first[i] != second[i]:
            temp = "F"
            break
        else:
            temp = "T"
    if temp == "F":
        print("Impossible")
    else:
        print("Possible")