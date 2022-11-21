def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        for j in range(food[i] // 2):
            answer += str(i)
    
    reverse_answer = answer[::-1]
    answer += '0' + reverse_answer
    
    
    return answer