def solution(number, limit, power):
    total_iron = 0

    for i in range(1,number+1):
        div=0
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                div+=1
                if j!=i//j:
                    div+=1
        attack= div if div<=limit else power
        total_iron+=attack
    
    return total_iron