def solution(cards1, cards2, goal):
    idx1 = idx2 = 0  # cards1, cards2의 현재 위치
    
    for word in goal:
        # cards1의 현재 카드와 일치하는 경우
        if idx1 < len(cards1) and cards1[idx1] == word:
            idx1 += 1
        # cards2의 현재 카드와 일치하는 경우
        elif idx2 < len(cards2) and cards2[idx2] == word:
            idx2 += 1
        # 둘 다 일치하지 않으면 불가능
        else:
            return "No"
    
    return "Yes"