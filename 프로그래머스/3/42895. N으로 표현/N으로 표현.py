def solution(N, number):
    # dp[i]: N을 i번 사용해서 만들 수 있는 숫자들의 집합
    dp = [set() for _ in range(9)]  # 1~8번 사용, 9 이상은 -1 반환
    
    # 초기화: N을 i번 반복한 숫자 (예: N=5, i=1 -> 5, i=2 -> 55)
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # N, NN, NNN, ...
        
        # 이전 결과들을 조합하여 새로운 숫자 생성
        for j in range(1, i):
            for x in dp[j]:  # j번 사용한 숫자
                for y in dp[i-j]:  # (i-j)번 사용한 숫자
                    dp[i].add(x + y)  # 덧셈
                    dp[i].add(x - y)  # 뺄셈
                    dp[i].add(x * y)  # 곱셈
                    if y != 0:  # 분모가 0이 아닌 경우
                        dp[i].add(x // y)  # 나눗셈 (나머지 무시)
        
        # 목표 숫자가 현재 집합에 있으면 i 반환
        if number in dp[i]:
            return i
    
    # 최솟값이 8보다 크면 -1 반환
    return -1