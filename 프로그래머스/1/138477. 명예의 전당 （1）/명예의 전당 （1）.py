def solution(k, score):
    answer = []
    lis = []
    
    for sc in score:
        # 점수 추가
        lis.append(sc)
        # 상위 k개 점수만 유지
        lis.sort(reverse=True)  # 내림차순 정렬
        lis = lis[:k]  # k개만 유지
        # 최소값 추가
        answer.append(min(lis))
    
    return answer