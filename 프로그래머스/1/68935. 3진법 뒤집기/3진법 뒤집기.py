def solution(n):
    # 3진법 변환
    ternary = ''
    while n:
        n, remainder = divmod(n, 3)
        ternary += str(remainder)
    
    # 앞뒤 뒤집기 (이미 뒤집힌 상태이므로 별도 뒤집기 불필요)
    # 10진법으로 변환
    return int(ternary, 3)