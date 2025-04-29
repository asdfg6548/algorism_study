def solution(s):
    # 숫자와 영단어를 매핑한 딕셔너리 (영단어를 숫자 문자열로 변환)
    num_dict = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    
    # 입력 문자열을 초기 결과로 설정
    result = s
    
    # 딕셔너리의 각 영단어와 숫자를 순회
    for word, num in num_dict.items():
        # 문자열에서 영단어를 해당 숫자로 치환
        result = result.replace(word, num)
    
    # 최종 문자열을 정수로 변환하여 반환
    return int(result)