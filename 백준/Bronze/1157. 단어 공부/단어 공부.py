word = input().upper() # 입력값을 다 대문자로 바꿈
dict = {}

# dict[알파벳] = 사용 횟수
for i in word:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1

most_cnt = max(dict.values()) # 최빈값의 등장 횟수

n = 0 # 최빈값의 개수
ans = 0 # 최빈값

for key, value in dict.items():
    if value == most_cnt:
        n += 1
        ans = key
        
# 최빈값이 2개 이상이면 ? 출력
if n>1:
    print('?')
else:
    print(ans)