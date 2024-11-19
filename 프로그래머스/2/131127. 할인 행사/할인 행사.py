def solution(want, number, discount):
    answer = 0
    dic = {}
    
    # 원하는 제품과 수량을 딕셔너리에 저장
    for i in range(len(want)):
        dic[want[i]] = number[i]
    
    # discount 배열을 10개씩 슬라이딩하며 확인
    for i in range(len(discount) - 9):
        temp_dic = dic.copy()  # 원본 딕셔너리 복사
        
        # 10일간의 할인 제품 확인
        for j in range(i, i + 10):
            if discount[j] in temp_dic:
                temp_dic[discount[j]] -= 1
        
        # 모든 제품의 수량이 0이 되었는지 확인
        if all(value == 0 for value in temp_dic.values()):
            answer += 1
    
    return answer