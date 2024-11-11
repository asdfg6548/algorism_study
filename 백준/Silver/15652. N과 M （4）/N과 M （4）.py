n,m=map(int,input().split())
res=[]

def backtracking(start):
    if len(res)==m:
        print(' '.join(map(str,res)))
        return

    for i in range(start,n+1):
        res.append(i)
        backtracking(i)
        res.pop()

backtracking(1)