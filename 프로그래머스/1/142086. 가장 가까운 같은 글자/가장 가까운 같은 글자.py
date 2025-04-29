def solution(s):
    # 문자별 가장 최근 등장 인덱스를 저장할 딕셔너리
    last_seen = {}
    # 결과를 저장할 리스트
    result = []
    
    # 문자열 s를 인덱스와 문자 단위로 순회
    for i, char in enumerate(s):
        # 현재 문자가 이전에 등장했는지 확인
        if char in last_seen:
            # 현재 인덱스(i)와 이전 등장 인덱스(last_seen[char])의 차이(거리)를 추가
            result.append(i - last_seen[char])
        else:
            # 첫 등장인 경우 -1 추가
            result.append(-1)
        # 현재 문자의 인덱스를 딕셔너리에 저장 (갱신)
        last_seen[char] = i
    
    # 결과 리스트 반환
    return result