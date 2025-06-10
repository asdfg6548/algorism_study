import sys
input = sys.stdin.readline

n = int(input())
count=0

# 5kg 봉지를 최대한 사용
while n >= 5:
    n -= 5
    count += 1

# 5kg 봉지 사용 개수를 줄이며 3kg 봉지로 채울 수 있는지 확인
while count >= 0:
    if n % 3 == 0:  # 남은 무게가 3kg 봉지로 정확히 채워지면
        count += n // 3
        print(count)
        exit()
    n += 5  # 5kg 봉지 하나 반환
    count -= 1

# 모든 경우를 확인했는데도 불가능하면 -1
print(-1)