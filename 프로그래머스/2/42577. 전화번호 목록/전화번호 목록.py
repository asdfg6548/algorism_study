def solution(phone_book):
    phone_book.sort()  # 전화번호부를 사전순으로 정렬
    
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    
    return True