import sys
input=sys.stdin.readline

N = int(input())  # 입력 받기
lis = list(map(int, input().split()))  # 수열을 리스트로 변환
result = [-1] * N  # 결과를 저장할 리스트 (기본값은 -1)
stack = []  # 인덱스를 저장할 스택

for i in range(N):
    while stack and lis[i] > lis[stack[-1]]:  # 스택이 비어 있지 않고, 현재 원소가 스택의 맨 위 원소보다 클 때
        result[stack[-1]] = lis[i]  # 스택의 맨 위 인덱스에 해당하는 원소의 오큰수를 현재 원소로 설정
        stack.pop()  # 스택에서 맨 위 원소를 제거
    stack.append(i)  # 현재 인덱스를 스택에 추가
print(*result)  # 결과 출력