def solution(s):
    answer = ''
    
    s=list(s)
    if len(s)%2!=0:
        idx=len(s)//2
        return s[idx]
    else:
        idx=len(s)//2
        return s[idx-1]+s[idx]
    return answer