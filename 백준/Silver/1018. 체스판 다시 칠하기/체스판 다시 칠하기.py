def min_repaint(board, N, M):
    min_changes = float('inf')  # 최소 변경 횟수 초기화
    
    # 가능한 모든 8x8 시작점 탐색
    for i in range(N - 7):
        for j in range(M - 7):
            changes1 = 0  # 패턴 1: 맨 왼쪽 위가 'W'
            changes2 = 0  # 패턴 2: 맨 왼쪽 위가 'B'
            
            # 8x8 부분 보드 확인
            for r in range(8):
                for c in range(8):
                    current = board[i + r][j + c]  # 현재 칸의 색
                    # 패턴 1: (r+c)가 짝수면 'W', 홀수면 'B'
                    expected1 = 'W' if (r + c) % 2 == 0 else 'B'
                    # 패턴 2: (r+c)가 짝수면 'B', 홀수면 'W'
                    expected2 = 'B' if (r + c) % 2 == 0 else 'W'
                    
                    # 색이 다르면 변경 횟수 증가
                    if current != expected1:
                        changes1 += 1
                    if current != expected2:
                        changes2 += 1
            
            # 최소 변경 횟수 갱신
            min_changes = min(min_changes, changes1, changes2)
    
    return min_changes

# 입력 처리
N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

# 결과 출력
print(min_repaint(board, N, M))