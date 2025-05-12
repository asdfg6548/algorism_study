from itertools import combinations

def is_prime(n):
    # 2 미만의 수는 소수가 아님
    if n < 2:
        return False
    # 2부터 √n까지 약수 확인
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    
    # 3개의 수를 선택한 조합
    lis = list(combinations(nums, 3))
    
    # 각 조합의 합 계산
    for comb in lis:
        if is_prime(sum(comb)):
            answer += 1
                
    return answer