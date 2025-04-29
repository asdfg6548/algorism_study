def solution(price, money, count):
    res =0
    sum_price=0
    for i in range(1,count+1):
        sum_price+=(price*i)
    
    if sum_price-money>0:
        res=sum_price-money
        
    else:
        res=0
    
    return res