from collections import deque
from itertools import combinations
import sys
input=sys.stdin.readline

target = int(input())
n = int(input())
break_num = list(map(int, input().split()))

res=abs(100-target)

for nums in range(1000001):
    nums=str(nums)
    
    for j in range(len(nums)):
        if int(nums[j]) in break_num:
            break
        elif j==len(nums)-1:
            res=min(res,len(nums)+abs(int(nums)-target))
        
print(res)