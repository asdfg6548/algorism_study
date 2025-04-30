def solution(name, yearning, photo):
    
    score_dict=dict(zip(name,yearning))
    
    answer=[]
    
    for people in photo:
        total_score=sum( score_dict.get(person,0) for person in people)
        answer.append(total_score)
    
    return answer