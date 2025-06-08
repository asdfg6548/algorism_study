import sys
input = sys.stdin.readline

# 입력: N (N번째 종말의 수를 찾기 위함)
N = int(input().strip())

# 종말의 수 찾기
count = 0  # 종말의 수 개수
num = 666  # 시작 수 (최소 종말의 수)

while True:
    # 현재 숫자에 "666"이 포함되어 있는지 확인
    if "666" in str(num):
        count += 1  # 종말의 수 발견
        if count == N:  # N번째 종말의 수라면
            print(num)  # 출력 후 종료
            break
    num += 1  # 다음 숫자로 이동