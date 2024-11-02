# 순열을 활용
from itertools import permutations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = range(1, n+1)

# permutations를 사용하여 1부터 n까지의 수 중에서 m개를 선택하는 모든 순열을 생성
for perm in permutations(numbers, m):
    print(' '.join(map(str, perm)))