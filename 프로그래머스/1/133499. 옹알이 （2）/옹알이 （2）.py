def solution(babbling):
    # 가능한 발음 리스트
    sounds = ["aya", "ye", "woo", "ma"]
    count = 0  # 발음할 수 있는 단어의 개수
    
    for word in babbling:  # 각 단어에 대해 처리
        i = 0  # 단어 내 현재 위치
        prev_sound = ""  # 이전에 사용한 발음 (연속 발음 체크용)
        
        while i < len(word):  # 단어 끝까지 탐색
            found = False  # 현재 위치에서 발음 찾았는지 여부
            for sound in sounds:  # 가능한 발음들 확인
                # 현재 위치에서 sound와 일치하고, 이전 발음과 다를 경우
                if  word[i:i+len(sound)] == sound and sound != prev_sound:
                    i += len(sound)  # 해당 발음 길이만큼 이동
                    prev_sound = sound  # 이전 발음 갱신
                    found = True
                    break
            if not found:  # 어떤 발음도 매칭되지 않으면
                break  # 이 단어는 발음 불가능
            
            if i == len(word):  # 단어 끝까지 도달하면
                count += 1  # 발음 가능한 단어로 카운트
    
    return count  # 발음 가능한 단어 개수 반환