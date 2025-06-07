import sys
input = sys.stdin.readline
import math

A,B,V=map(int,input().split())

high=V-A
sum_len=A-B

res=math.ceil(high/sum_len)+1

print(res)