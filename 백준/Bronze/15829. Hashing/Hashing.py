import sys
input = sys.stdin.readline

n = int(input())  # 문자열 길이
s = input().strip()  # 문자열 입력 (개행 문자 제거)
mod = 1234567891
res = 0

for i in range(n):
    num = ord(s[i]) - 96  # a=1, b=2, ..., z=26
    res = (res + num * pow(31, i)) % mod  # a_i * 31^i mod M을 계산 후 합산

print(res)