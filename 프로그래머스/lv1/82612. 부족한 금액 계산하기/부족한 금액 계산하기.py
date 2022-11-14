def solution(price, money, count):
    answer = -1
    useAmount = 0
    
    for i in range(1, count+1):
        useAmount += price * i
    
    answer = useAmount - money
    
    if answer > 0:
        return answer
    else:
        return 0