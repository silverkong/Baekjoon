def solution(n):
    answer = ''
    n = list(str(n))
    n.sort(reverse=True)
    
    for num in n:
        answer += num
    
    return int(answer)