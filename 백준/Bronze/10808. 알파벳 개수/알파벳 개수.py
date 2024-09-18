import sys
input = sys.stdin.readline

al_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word = input().rstrip()  # 줄바꿈 문자 제거

# 빈도수 계산
frequency = {char: 0 for char in al_list}
for char in word:
    if char in frequency:
        frequency[char] += 1

# 결과 출력
for char in al_list:
    print(frequency[char], end=" ")
