def solution(n):
    answer = 0
    arr=[]
    for x in range(2,n+1):
        if n%x==1:
            arr.append(x)
        
    answer=arr[0]
    return answer