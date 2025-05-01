def solution(babbling):
    answer = 0  # 발음할 수 있는 단어의 개수 초기화
    for i in babbling:  # 각 단어에 대해 반복
        for j in ['aya', 'ye', 'woo', 'ma']:  # 가능한 발음 리스트 탐색
            # 연속된 같은 발음(예: "ayaaya", "yeye")이 단어에 없는 경우
            if j*2 not in i:
                # 해당 발음을 공백(' ')으로 치환
                i = i.replace(j, ' ')
        # 치환 후 공백을 제거한 문자열의 길이가 0이면 발음 가능한 단어
        if len(i.strip()) == 0:
            answer += 1  # 발음 가능한 단어 개수 증가
    return answer  # 최종 발음 가능한 단어 개수 반환