n=int(input())

cnt=1
num_box=1

while n>num_box:
    num_box=num_box+6*(cnt)
    cnt+=1

print(cnt)