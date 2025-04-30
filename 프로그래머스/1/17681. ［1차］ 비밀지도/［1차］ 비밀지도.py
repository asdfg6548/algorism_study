def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # 두 지도의 해당 행을 비트 OR 연산
        row = arr1[i] | arr2[i]
        # 이진수로 변환하고 n비트로 맞춤
        binary = bin(row)[2:].zfill(n)
        # 1은 '#', 0은 ' '로 변환
        line = ''.join('#' if bit == '1' else ' ' for bit in binary)
        answer.append(line)
    return answer