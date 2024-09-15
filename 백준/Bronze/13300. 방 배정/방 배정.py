import sys
input = sys.stdin.readline

n,m=map(int,input().split())
res=0

# 각 학년 담을 배열
girls = [0] * 7
boys = [0] * 7

# 입력받기, 학생수만큼 돌면서 성별맞춰서 넣어주기 (학년 별 학생 수만 저장)
for i in range(n):
    a,b=map(int,input().split())
    if a==0:
        girls[b]+=1
    else:
        boys[b]+=1

# 받은거 나누기
room = 0
for i in range(7):
    # 나머지 있으면 방하나 추가하고, 없으면 그냥 몫만! 0도 자연스럽게 걸러짐
    if girls[i] % m:
        room += ((girls[i] // m) + 1)
    else:
        room += girls[i] // m

    if boys[i] % m:
        room += ((boys[i] // m) + 1)
    else:
        room += boys[i] // m

print(room)
