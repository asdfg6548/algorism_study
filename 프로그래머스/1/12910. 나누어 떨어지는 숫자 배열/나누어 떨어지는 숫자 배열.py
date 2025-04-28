def solution(arr, divisor):
    answer = []
    
    for s in arr:
        if s%divisor==0:
            answer.append(s)
    
    if answer:
        answer.sort()
    else:
        answer.append(-1)
    
    return answer