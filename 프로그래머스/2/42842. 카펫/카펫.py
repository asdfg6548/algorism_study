def solution(brown, yellow):
    # x는 가로 y는 세로 가로가 더 크거나 같음
    for x in range(3,brown//2):
        for y in range(3,brown//2):
            if(((2*x)+(2*y)-4==brown) and ((x-2)*(y-2)==yellow) and(x>=y)):
                return [x,y]