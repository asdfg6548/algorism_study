def solution(s):
    # 길이가 4 또는 6인지 확인
    if len(s) != 4 and len(s) != 6:
        return False
    # 숫자로만 구성되어 있는지 확인
    for char in s:
        if not char.isdigit():
            return False
    return True