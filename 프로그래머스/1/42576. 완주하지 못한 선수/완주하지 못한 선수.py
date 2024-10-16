def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i]!=completion[i]:
            res=participant[i]
            return res
        
    return participant[-1]