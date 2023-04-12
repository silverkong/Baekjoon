def solution(order):
    temp = []
    i = 1
    answer = 0
    
    while i != len(order) + 1:
        temp.append(i)
        while temp[-1] == order[answer]:
            answer += 1
            temp.pop()
            
            if len(temp) == 0:
                break
        i += 1
        
    return answer