def solution(priorities, location):
    answer = 0  # 실행 순서를 카운트하는 변수 초기화
    place = priorities.index(max(priorities))  # 첫 번째 최대 우선순위의 인덱스를 찾음
    
    while (True):  # 무한 루프 시작
        value = max(priorities)  # 현재 우선순위 리스트에서 최대값 찾기
        
        if priorities[place] == value:  # 현재 위치의 우선순위가 최대값과 같은 경우
            priorities[place] = 0  # 해당 프로세스 실행 완료 처리 (우선순위를 0으로 설정)
            answer += 1  # 실행 순서 증가
            
            if place == location:  # 현재 위치가 요청한 location과 같으면
                break  # 루프 종료
        
        place += 1  # 다음 위치로 이동
        
        if place >= len(priorities):  # place가 리스트 길이를 초과하면
            place = 0  # 처음 위치로 돌아감 (순환 큐처럼 동작)
    
    return answer  # 요청한 location의 프로세스가 실행된 순서 반환