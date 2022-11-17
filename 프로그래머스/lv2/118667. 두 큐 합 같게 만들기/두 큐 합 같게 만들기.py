from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    sumQ1, sumQ2 = sum(queue1), sum(queue2)
    sumQueue = (sumQ1 + sumQ2) // 2
    limit = len(queue1) * 3
    
    while True:
        if sumQ1 > sumQ2:
            temp = queue1.popleft()
            queue2.append(temp)
            sumQ1 -= temp
            sumQ2 += temp
            answer += 1
        elif sumQ1 < sumQ2:
            temp = queue2.popleft()
            queue1.append(temp)
            sumQ1 += temp
            sumQ2 -= temp
            answer += 1
        else:
            break
        
        if answer == limit:
            answer = -1
            break
    
    return answer