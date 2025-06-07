import sys
input = sys.stdin.readline

def sol(k,n):
    # dp 테이블 생성
    residents=[[0]*(n+1) for i in range(k+1)]

    # 0층 인원 수 초기화
    for i in range(n+1):
        residents[0][i]=i

    # 1층부터 k층 인원수 계산
    for floor in range(1,k+1):
        for num in range(1,n+1):
            # 각 호수의 사람 수 = 같은 층 이전 호수 + 아래층 같은 호수
            residents[floor][num]=residents[floor][num-1]+residents[floor-1][num]

    # 인원수 반환
    return residents[k][n]

T = int(input())  # 테스트 케이스 수
for _ in range(T):
    k = int(input())  # 층 수
    n = int(input())  # 호 수
    print(sol(k, n))