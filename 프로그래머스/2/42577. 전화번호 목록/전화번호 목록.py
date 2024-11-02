def solution(phone_book):
    hash_map = set(phone_book)

    for phone_number in phone_book:
        temp = ""
        for digit in phone_number[:-1]:  # 마지막 숫자를 제외한 모든 숫자에 대해
            temp += digit
            if temp in hash_map:
                return False

    return True