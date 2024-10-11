def solution(sizes):
    answer = 0
    # 가로와 세로 값들 저장 리스트
    garo=[]
    sero=[]
    
    # 명함을 돌릴 수 있으므로 큰 값을 전부 가로에
    # 가로보다 세로가 크면 값을 바꿈
    # 그 후 리스트에 추가
    for i in range(len(sizes)):
        if sizes[i][0]<sizes[i][1]:
            tmp=sizes[i][0]
            sizes[i][0]=sizes[i][1]
            sizes[i][1]=tmp
        garo.append(sizes[i][0])
        sero.append(sizes[i][1])
    
    # 가로의 최대값과 세로의 최대값을 곱함
    answer=max(garo)*max(sero)
    return answer