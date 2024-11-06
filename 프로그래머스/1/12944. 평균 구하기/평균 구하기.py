def solution(arr):
    answer = 0
    res=0
    cnt=0
    
    for i in arr:
        res+=i
        cnt+=1
        
    answer=res/cnt
    return answer