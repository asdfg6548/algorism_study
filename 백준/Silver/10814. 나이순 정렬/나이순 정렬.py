import sys
input = sys.stdin.readline

# 회원 수 N 입력받기
n = int(input())

# 회원 정보를 저장할 리스트
members = []

# N개의 줄에 걸쳐 나이와 이름을 입력받아 리스트에 추가
for i in range(n):
    age, name = input().split()
    members.append((int(age), i, name))  # (나이, 가입 순서, 이름)

# 나이 기준 오름차순, 나이가 같으면 가입 순서 기준으로 정렬
members.sort(key=lambda x: (x[0], x[1]))

# 정렬된 회원 정보를 출력
for member in members:
    print(member[0], member[2])