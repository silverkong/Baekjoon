def solution(n):
    answer = []
    n = str(n)[::-1]
    
    for num in n:
        answer.append(int(num))
    
    return answer