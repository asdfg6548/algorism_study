def solution(s):
    answer = []
    li=[]
    
    for i in s.split("},"):
        li.append(i.replace("{","").replace("}","").split(","))
    
    li.sort(key=len)
   
    for i in li:
        for j in i:
            if j not in answer:
                answer.append(j)
    return list(map(int,answer))
