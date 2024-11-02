def solution(numbers):
    
    # 숫자들을 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 정렬 기준을 정의: 두 수를 이어 붙였을 때 더 큰 수를 만드는 순서
    numbers.sort(key=lambda x: x*5, reverse=True)
    
    # 정렬된 숫자들을 이어 붙여 결과 생성
    answer = ''.join(numbers)
    
    # 결과가 모두 0으로 구성된 경우 "0"을 반환
    return "0" if answer[0] == "0" else answer