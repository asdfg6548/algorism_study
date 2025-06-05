def gcd(a, b):
    # 유클리드 알고리즘으로 최대공약수 계산
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # 최소공배수 = (a * b) / GCD(a, b)
    return (a * b) // gcd(a, b)

# 입력 처리
a, b = map(int, input().split())

# 최대공약수와 최소공배수 출력
print(gcd(a, b))
print(lcm(a, b))