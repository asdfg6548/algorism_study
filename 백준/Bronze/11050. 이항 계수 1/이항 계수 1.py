from math import comb

# 입력 처리
n, k = map(int, input().split())

# 결과 출력
print(comb(n, k))