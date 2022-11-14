import math

def solution(n):
    answer = 0
    
    for i in range(n + 1):
        if solve(i):
            answer += 1
    
    return answer

def solve(n):
    if n < 2:
        return False
    
    if n == 2:
        return True
        
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True