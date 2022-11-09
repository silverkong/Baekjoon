def solution(arr):
    answer = []
    print(len(answer))
    
    for a in arr:
        if len(answer) == 0:
            answer.append(a)
        elif answer[len(answer)-1] != a:
            answer.append(a)
    
    return answer