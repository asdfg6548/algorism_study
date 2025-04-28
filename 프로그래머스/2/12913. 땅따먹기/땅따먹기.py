def solution(land):
    n=len(land)
    dp=[[0]*4 for i in range(n)]
    
    for j in range(4):
        dp[0][j]=land[0][j]
        
    for i in range(1,n):
        for j in range(4):
            if j==0:
                max_prev=max(dp[i-1][1],dp[i-1][2],dp[i-1][3])
            elif j==1:
                max_prev=max(dp[i-1][0],dp[i-1][2],dp[i-1][3])
            elif j==2:
                max_prev=max(dp[i-1][0],dp[i-1][1],dp[i-1][3])
            elif j==3:
                max_prev=max(dp[i-1][0],dp[i-1][1],dp[i-1][2])
                
            dp[i][j]=land[i][j]+max_prev
    return max(dp[n-1])