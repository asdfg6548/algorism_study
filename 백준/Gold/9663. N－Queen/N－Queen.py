N = int(input())  # N은 체스판의 크기이자 퀸의 개수

arr = [0] * N  # arr 배열은 각 행(row)에서 퀸이 위치한 열(column)을 기록

def is_possible(r):
    # 현재 row(r)에 퀸을 놓았을 때, 이전 행들과의 충돌 여부를 검사하는 함수
    for i in range(r):  # 이전 행들(i)에 배치된 퀸들과 비교
        # 같은 열에 있는지 확인 (arr[r] == arr[i])
        if arr[r] == arr[i]:
            return False
        # 대각선에 있는지 확인 (r - i == abs(arr[r] - arr[i]))
        # 행 차이와 열 차이의 절대값이 같으면 대각선에 있는 것임
        if r - i == abs(arr[r] - arr[i]):
            return False
    return True  # 충돌하지 않으면 True 반환


def dfs(row):
    # row는 현재 처리 중인 행의 번호
    # row가 N에 도달하면 모든 퀸을 배치한 것이므로 1을 반환
    if row == N:
        return 1  # N개의 퀸을 모두 배치한 경우

    ans = 0  # 가능한 배치의 경우의 수를 저장하는 변수
    for i in range(N):  # 각 열(i)에 퀸을 배치 시도
        arr[row] = i  # 현재 row에 퀸을 i번째 열에 배치
        if is_possible(row):  # 현재 배치가 가능한지 확인
            ans += dfs(row + 1)  # 가능하다면 다음 행으로 이동(dfs 재귀 호출)

    return ans  # 가능한 모든 경우의 수 반환


print(dfs(0))  # 0번째 행부터 시작하여 N개의 퀸을 배치하는 경우의 수 출력