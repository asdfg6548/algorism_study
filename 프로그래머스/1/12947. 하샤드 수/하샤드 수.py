def solution(x):
    answer = False
    # 변수 설정
    ls=list(str(x))
    sum_ls = 0
            
    # 문자열 숫자로 변환해서 하나씩 더하기
    for i in ls:
        sum_ls+=int(i)
    # 자릿수들의 합으로 나눠지는지 확인
    if x%sum_ls==0:
        answer=True
    
    return answer