from itertools import permutations
def solution(k, dungeons):
    max_num=0
    lis=list(permutations(dungeons,len(dungeons)))
    
    for i in range(len(lis)):
        num=0
        check=k
        
        for min_p,lost_p in lis[i]:
            if check>=min_p:
                check-=lost_p
                num+=1
        
        if num>max_num:
            max_num=num
    return max_num