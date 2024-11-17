def solution(k, tangerine):
    answer = 0
    dic={}
    nums=0
    
    for i in tangerine:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
            
    arr=sorted(dic.items(),key=lambda x :x[1], reverse=True)
    
    for a in arr:
        nums+=a[1]
        answer+=1
        if nums>=k:
            break
    
    return answer