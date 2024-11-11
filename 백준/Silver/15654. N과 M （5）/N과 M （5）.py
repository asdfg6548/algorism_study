# n은 선택할 수 있는 숫자의 범위 (1부터 n까지), m은 선택할 숫자의 개수
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []  # 결과를 저장할 리스트


# 백트래킹 함수 정의
def backtracking():
    if len(res) == m:  # 종료 조건: res에 m개의 숫자가 모두 선택된 경우
        print(' '.join(map(str, res)))  # 선택된 숫자들을 출력
        return  # 재귀 종료

    # arr 안의 숫자들 중에서 선택
    for i in arr:
        if i not in res:  # 중복되지 않도록 숫자가 이미 res에 없는 경우에만 추가
            res.append(i)  # 숫자 i를 선택
            backtracking()  # 선택된 숫자를 기준으로 다시 재귀 호출
            res.pop()  # 선택된 숫자를 제거하고 다음 숫자를 시도 (백트래킹)


# 백트래킹 함수 실행
backtracking()