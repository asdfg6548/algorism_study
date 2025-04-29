# 제곱수 이면 약수의 개수가 홀수 아니면 짝수
def solution(left, right):
    answer = 0
    for num in range(left, right + 1):
        # 완전제곱수인지 확인
        if int(num ** 0.5) ** 2 == num:
            answer -= num  # 약수 개수 홀수
        else:
            answer += num  # 약수 개수 짝수
    return answer