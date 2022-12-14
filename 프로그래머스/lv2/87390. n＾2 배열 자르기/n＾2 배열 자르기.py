def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        a, b = i // n, i % n
        c = max(a, b)
        answer.append(c + 1)
    
    return answer