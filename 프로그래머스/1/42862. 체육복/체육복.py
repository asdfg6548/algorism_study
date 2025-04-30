def solution(n, lost, reserve):
    # 여벌 체육복이 있지만 도난당한 학생 처리
    lost_set = set(lost) - set(reserve)  # 도난당한 학생 중 여벌 없는 학생
    reserve_set = set(reserve) - set(lost)  # 여벌 있는 학생 중 도난당하지 않은 학생
    
    # 초기 체육수업 참여 가능 학생 수: 전체 학생 - 도난당한 학생
    answer = n - len(lost_set)
    
    # 여벌 체육복을 빌려주기
    for lost_student in sorted(lost_set):
        # 앞번호 학생이 여벌 체육복이 있는지 확인
        if lost_student - 1 in reserve_set:
            reserve_set.remove(lost_student - 1)
            answer += 1
        # 뒷번호 학생이 여벌 체육복이 있는지 확인
        elif lost_student + 1 in reserve_set:
            reserve_set.remove(lost_student + 1)
            answer += 1
    
    return answer