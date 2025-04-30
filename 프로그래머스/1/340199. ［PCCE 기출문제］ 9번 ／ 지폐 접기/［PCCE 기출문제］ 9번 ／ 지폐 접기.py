def solution(wallet, bill):
    answer = 0
    
    # 지폐를 지갑에 넣을 수 있을 때까지 반복
    while (min(bill) > min(wallet) or max(bill) > max(wallet)):
        # 긴 쪽을 반으로 접음
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2  # 홀수면 소수점 이하 버림
        else:
            bill[1] = bill[1] // 2  # 홀수면 소수점 이하 버림
        answer += 1
    
    return answer