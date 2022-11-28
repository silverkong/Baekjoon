def solution(d, budget):
    answer = 0
    temp = 0
    d.sort()
    
    for dd in d:
        temp += dd
        if temp <= budget:
            answer += 1
    
    return answer