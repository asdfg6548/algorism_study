n, m = map(int, input().split())
res = []  # 결과를 저장할 리스트

# 백트래킹 함수 정의
def backtracking():
    if len(res) == m:  # 종료 조건: res에 m개의 숫자가 모두 선택된 경우
        print(' '.join(map(str, res)))  # 선택된 숫자들을 출력
        return  # 재귀 종료

    # 1부터 n까지의 숫자들 중에서 중복 허용하여 선택
    for i in range(1, n + 1):
        # if i not in res (X) -> 중복이 가능하게
        res.append(i)  # 숫자 i를 선택
        backtracking()  # 선택된 숫자를 기준으로 다시 재귀 호출
        res.pop()  # 선택된 숫자를 제거하고 다음 숫자를 시도 (백트래킹)

# 백트래킹 함수 실행
backtracking()

