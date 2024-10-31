def solution(skill, skill_trees):
    answer = 0
    
    here=[]
    lv=''
    
    for i in skill:
        lv+=i
        here.append(lv)
    
    temp=[]
    for idx in skill_trees:
        a=[s for s in idx]
        ans=''
        
        for sk in a:
            if sk in skill:
                ans+=sk
        temp.append(ans)
                
    for idx in temp:
        if idx in here:
            answer+=1
        if idx=='':
            answer+=1
    
    return answer