import sys
input = sys.stdin.readline


n=int(input()) 
l=list(map(int,input().split()))
ans=[0 for i in range(n)]

stack=[ (l[0],1) ] #높이, index)

#같은 타워도 통과함 
for i in range(1,n):
    #하나를 넣어주고 시작하기 때문에 여기서 len(stack)인 경우는 없음
    
    if l[i]<stack[-1][0]: #편하게 추가하는 경우
        ans[i]=stack[-1][1] #정답은 index로 담아줌
        stack.append((l[i],i+1)) #현재 높이와index 담아줌
    else: #통과
        while True:
            stack.pop()
            if len(stack)==0: 
                stack.append((l[i],i+1))
                break
            if l[i]<stack[-1][0] : 
                ans[i]=stack[-1][1]
                stack.append((l[i],i+1))
                break
   
print(*ans)


