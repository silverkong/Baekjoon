import math

def solution(n, k):
    answer = 0
    baseK = ''
    
    while n > 0:
        n, mod = divmod(n, k)
        baseK += str(mod)
        
    baseK = baseK[::-1]
    checkList = [i for i in baseK.split('0')]
    
    for num in checkList:
        if num == '1' or num == '':
            continue
        else:
            check = primeNum(int(num))
            if check:
                answer += 1
        
    return answer

def primeNum(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
        
    return True