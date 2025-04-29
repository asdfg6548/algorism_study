def solution(s, n):
    # 소문자 알파벳 리스트 (a-z, 0~25 인덱스)
    lower_list = "abcdefghijklmnopqrstuvwxyz"
    # 대문자 알파벳 리스트 (A-Z, 0~25 인덱스)
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # 변환된 문자를 저장할 리스트
    result = []

    # 문자열 s의 각 문자를 순회
    for i in s:
        # 공백인 경우: 그대로 result에 추가
        if i == " ":
            result.append(" ")
        # 소문자인 경우
        elif i.islower() is True:
            # lower_list에서 현재 문자의 인덱스 찾기
            new_ = lower_list.find(i) + n
            # n만큼 밀고, 26으로 나눈 나머지로 순환 처리 후 해당 문자 추가
            result.append(lower_list[new_ % 26])
        # 대문자인 경우
        else:
            # upper_list에서 현재 문자의 인덱스 찾기
            new_ = upper_list.find(i) + n
            # n만큼 밀고, 26으로 나눈 나머지로 순환 처리 후 해당 문자 추가
            result.append(upper_list[new_ % 26])
    
    # result 리스트를 문자열로 결합하여 반환
    return "".join(result)