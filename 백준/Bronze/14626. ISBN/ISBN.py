import sys
input = sys.stdin.readline

# 입력: 13자리 ISBN 문자열 (숫자와 '*' 포함)
n = input().strip()

# 변수 초기화
num = 0          # 가중치 적용 후 숫자 합 (체크기호 제외)
star_pos = 0     # '*'의 위치 (1-based index)
check_digit = 0  # 체크기호 (마지막 자리)

# 입력 문자열 순회
for i in range(13):
    s = n[i]
    if s == '*':
        star_pos = i + 1  # '*' 위치 기록 (1-based)
    else:
        digit = int(s)
        if i == 12:  # 마지막 자리 (체크기호)
            check_digit = digit
        else:  # 체크기호 제외한 자리
            if (i + 1) % 2 == 0:  # 짝수 번째 자리 (가중치 3)
                num += 3 * digit
            else:  # 홀수 번째 자리 (가중치 1)
                num += digit

# 체크기호 공식: sum + m ≡ 0 (mod 10)
# num은 체크기호를 제외한 합, m은 체크기호
# '*' 자리 숫자를 x라 하면:
# 홀수 번째일 경우: num + x + m ≡ 0 (mod 10) → x = (10 - (num + m)) % 10
# 짝수 번째일 경우: num + 3x + m ≡ 0 (mod 10) → 3x = (10 - (num + m)) % 10 → x = (10 - (num + m)) * mod_inverse(3, 10) % 10
if star_pos % 2 == 0:  # '*'가 짝수 번째 자리
    # 3x ≡ (10 - (num + check_digit)) (mod 10)
    # 3의 모듈러 역수(mod 10)는 7 (since 3 * 7 = 21 ≡ 1 (mod 10))
    target = (10 - (num + check_digit)) % 10
    x = (target * 7) % 10  # x = target * mod_inverse(3, 10)
else:  # '*'가 홀수 번째 자리
    # x ≡ (10 - (num + check_digit)) (mod 10)
    x = (10 - (num + check_digit)) % 10

print(x)  # 결과 출력