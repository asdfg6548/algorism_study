# N은 퇴사까지 남은 날 수
N = int(input())
# Ti는 상담에 걸리는 기간, Pi는 상담을 했을 때 받을 수 있는 금액
T, P = [], []
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

# dp[i]는 i일째부터 퇴사일까지 얻을 수 있는 최대 이익을 저장
dp = [0] * (N + 1)

for i in range(N):
    # 상담을 하지 않는 경우, 다음 날의 dp값을 갱신
    dp[i + 1] = max(dp[i + 1], dp[i])

    # 상담을 할 수 있는 경우, 해당 상담을 반영하여 dp 갱신
    if i + T[i] <= N:
        dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i])

# 마지막 날까지 얻을 수 있는 최대 이익 출력
print(dp[N])
