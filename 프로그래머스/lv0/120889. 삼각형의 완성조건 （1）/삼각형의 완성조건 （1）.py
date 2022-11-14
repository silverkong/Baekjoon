def solution(sides):
    answer = 0
    maxSide = max(sides)
    del sides[sides.index(maxSide)]
    
    if sum(sides) <= maxSide:
        answer = 2
    else:
        answer = 1
    
    return answer