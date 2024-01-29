n,k=map(int,input().split())
res=[]
circle=[str(i+1) for i in range(n)]
for i in range(n):
     res.append(circle[(k-1) % len(circle)])
     circle = circle[(k-1) % len(circle)+1:]+circle[:(k-1) % len(circle)]


print('<'+', '.join(res)+'>')