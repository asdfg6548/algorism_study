def solution(answers):
    answer = []
    cnt1=0
    cnt2=0
    cnt3=0
    # 찍는 패턴 
    arr1=[1,2,3,4,5]
    arr2=[2,1,2,3,2,4,2,5]
    arr3=[3,3,1,1,2,2,4,4,5,5]
    
    # for 문을 돌며 확인하기
    for i in range(len(answers)):
        if answers[i]==arr1[i%5]:
            cnt1+=1
        if answers[i]==arr2[i%8]:
            cnt2+=1
        if answers[i]==arr3[i%10]:
            cnt3+=1
    # 점수 최대 값        
    Max=max(cnt1,cnt2,cnt3)
    
    #최대 점수를 받은 사람 찾기
    if Max==cnt1:
        answer.append(1)
    if Max==cnt2:
        answer.append(2)
    if Max==cnt3:
        answer.append(3)
    
    return answer