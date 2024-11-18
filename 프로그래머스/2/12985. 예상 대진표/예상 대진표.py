from math import ceil
def solution(n,a,b):
    answer = 0
    
    while True:
        answer+=1
        if abs(a-b)==1 and min(a,b) % 2 == 1:
            break
        else:
            a=ceil(a/2)
            b=ceil(b/2)

    return answer