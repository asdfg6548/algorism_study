from math import ceil  # 올림 함수 사용

def solution(n, a, b):
    answer = 0  # 라운드 수를 저장
    
    while True:
        answer += 1  # 라운드 증가
        # A와 B가 인접하고, 작은 번호가 홀수면 대결 조건 만족
        if abs(a - b) == 1 and min(a, b) % 2 == 1:
            break
        # 다음 라운드 번호로 갱신: 현재 번호를 2로 나누고 올림
        a = ceil(a / 2)
        b = ceil(b / 2)
    
    return answer  # A와 B가 만나는 라운드 번호 반환