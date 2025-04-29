# 왼쪽만 구한 후 -> 왼쪽 + 0 + 오른쪽
def solution(food):
    # 왼쪽 부분 문자열을 저장할 변수
    left = ""
    
    # food[1:]를 순회하며 각 음식의 개수를 절반으로 사용
    for i in range(1, len(food)):
        # 각 음식 i를 food[i]//2번 반복 (홀수일 경우 버림)
        left += str(i) * (food[i] // 2)
    
    # 왼쪽 문자열 + "0" (물) + 오른쪽 문자열(왼쪽 역순)
    answer = left + "0" + left[::-1]
    
    # 최종 문자열 반환
    return answer