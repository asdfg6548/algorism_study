def solution(phone_number):
    # 전체 길이에서 뒷 4자리를 제외한 길이만큼 '*' 생성
    mask_length = len(phone_number) - 4
    # 앞부분은 '*'로, 뒷 4자리는 원래 문자로 결합
    return '*' * mask_length + phone_number[-4:]