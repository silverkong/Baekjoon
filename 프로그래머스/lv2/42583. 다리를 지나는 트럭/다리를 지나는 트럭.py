from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    temp = 0
    bridge_queue = deque(bridge_length * [0])
    weights_queue = deque(truck_weights)
    
    while len(bridge_queue):
        answer += 1
        temp -= bridge_queue[0]
        bridge_queue.popleft()
        
        if weights_queue:
            if temp + weights_queue[0] <= weight:
                temp += weights_queue[0]
                bridge_queue.append(weights_queue.popleft())
            else:
                bridge_queue.append(0)
                
    return answer