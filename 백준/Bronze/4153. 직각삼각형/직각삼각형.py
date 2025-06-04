import sys
input = sys.stdin.readline

while True:
    # 입력 받기
    a, b, c = map(int, input().split())

    # 종료 조건: 0 0 0
    if a == 0 and b == 0 and c == 0:
        break

    # 세 변을 리스트로 만들어 정렬 (가장 긴 변을 c로 설정)
    sides = [a, b, c]
    sides.sort()
    a, b, c = sides

    # 피타고라스 정리 확인
    if a ** 2 + b ** 2 == c ** 2:
        print("right")
    else:
        print("wrong")