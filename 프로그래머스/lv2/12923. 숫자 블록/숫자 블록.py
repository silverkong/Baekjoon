import math

def solution(begin, end):
    answer = []
    
    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
            continue
        num = int(math.sqrt(end))
        for j in range(2, num + 1):
            if i // j > 10 ** 7:
                continue
            if i % j == 0:
                answer.append(i // j)
                break
        else:
            answer.append(1)
            
    return answer