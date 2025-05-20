import sys
input=sys.stdin.readline

# tower 값 리스트외에, stack[(탑의 인덱스,탑의 높이)] 을 하나 더 사용
## 오른쪽에서 왼쪽으로 레이저를 쏘므로 -> 더 높은 탑이 오른쪽에 있으면 왼쪽에 있는 낮은 탑은 레이저를 받을 수 없음 (스택에서 제거)
# stack에는 레이저를 받을 수 있는 탑들만 보관

n = int(input())
tower = list(map(int, input().split()))
stack = []
result = [0] * n  # 미리 크기 할당

for i in range(n):
    while stack and stack[-1][1] < tower[i]:  # 현재 탑보다 낮은 탑 제거
        stack.pop()
    
    if stack:  # 스택에 남은 탑이 있으면 수신 가능
        result[i] = stack[-1][0] + 1  # 1-based 인덱스
    # else: result[i] = 0 (기본값이 0이므로 생략 가능)
    
    stack.append((i, tower[i]))  # 현재 탑 추가

print(" ".join(map(str, result)))