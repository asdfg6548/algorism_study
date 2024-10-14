def solution(array, commands):
    answer = []
    res=[]
    
    for com in commands:
        res=array[com[0]-1:com[1]]
        res.sort()
        answer.append(res[com[2]-1])
        
    return answer