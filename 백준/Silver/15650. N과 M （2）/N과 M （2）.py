n, m = map(int, input().split())
res = []  # 결과를 저장할 리스트

# 백트래킹 함수 정의
def backtracking(start):
    if len(res) == m:  # 종료 조건: res에 m개의 숫자가 모두 선택된 경우
        print(' '.join(map(str, res)))  # 선택된 숫자들을 출력
        return  # 재귀 종료

    # start부터 n까지의 숫자들 중에서 선택
    for i in range(start, n + 1):
        if i not in res:  # 중복되지 않도록 숫자가 이미 res에 없는 경우에만 추가
            res.append(i)  # 숫자 i를 선택
            backtracking(i + 1)  # 다음 숫자는 i보다 큰 숫자만 선택하도록 설정
            res.pop()  # 선택된 숫자를 제거하고 다음 숫자를 시도 (백트래킹)

# 백트래킹 함수 실행 (시작점은 1부터)
backtracking(1)
