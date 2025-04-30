def solution(n, m, section):
    answer = 0
    covered=0
    
    for pos in section:
        # 이미 칠해진 구역이면 건너뛰기
        if pos <= covered:
            continue
        
        # 새 페인트칠 시작
        answer += 1
        
        # 현재 위치에서 롤러 길이만큼 칠함
        covered = pos + m - 1

    
    return answer