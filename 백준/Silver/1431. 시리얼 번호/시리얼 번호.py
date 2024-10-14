import sys

input = sys.stdin.readline

# n: 입력받을 문자열의 개수
n = int(input())

# arr: 입력받은 문자열들을 저장할 리스트
arr = []
for i in range(n):
    a = input().strip()  # 각 문자열 입력, 개행문자 제거 후 리스트에 추가
    arr.append(a)


# sum_num 함수: 주어진 문자열 내에서 숫자들을 모두 더하여 반환하는 함수
def sum_num(inputs):
    result = 0
    # 입력된 문자열에서 각 문자를 하나씩 확인
    for i in inputs:
        # 문자가 숫자인지 확인 (숫자인 경우 True 반환)
        if i.isdigit():
            # 숫자라면 정수형으로 변환 후 result에 더함
            result += int(i)
    return result


# arr 리스트를 정렬하는 과정
# key 함수는 3가지 기준으로 정렬을 진행
# 1. 문자열의 길이(len(x))를 기준으로 먼저 정렬
# 2. 문자열에 포함된 숫자들의 합(sum_num(x))을 기준으로 정렬
# 3. 마지막으로 문자열 자체를 사전순으로 정렬
arr.sort(key=lambda x: (len(x), sum_num(x), x))

# 정렬된 결과 출력
for i in arr:
    print(i)
