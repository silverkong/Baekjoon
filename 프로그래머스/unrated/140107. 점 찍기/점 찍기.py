import math

def solution(k, d):
    answer = 0
    
    for i in range(0, d + 1, k):
        l = math.sqrt(d * d - i * i)
        answer += (l // k) + 1
    
    return answer