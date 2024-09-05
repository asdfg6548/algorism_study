import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = 0
a.sort()

# max 함수를 이용해 b 리스트 가장 큰 수에 접근 -> B 정렬X
for i in a:
  tmp = i*max(b)
  res += tmp
  b.remove(max(b))

print(res)