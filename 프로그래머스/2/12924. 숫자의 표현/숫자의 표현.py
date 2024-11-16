def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        nums=0
        for j in range(i,n+1):
            nums+=j
            if nums==n:
                answer+=1
            if nums > n:           
                break
    
    return answer