def solution(s):
    zero_cnt=0
    change_cnt=0
    
    while s!="1":
        zero_cnt+=s.count("0")
        s=bin(s.count("1"))[2:]
        change_cnt+=1
    
    return [change_cnt,zero_cnt]