n=int(input())
m=int(input())
k=int(input())


num=n*m*k
res=list(str(num))

for i in range(10):
    print(res.count(str(i)), end="\n")
