import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 변수 초기화
start = 0
end = 0
current_sum = 0
res = 0

while True:
    if current_sum == m:
        res += 1
        current_sum -= arr[start]
        start += 1
    elif current_sum > m:
        current_sum -= arr[start]
        start += 1
    elif end < n:
        current_sum += arr[end]
        end += 1
    else:
        break

print(res)