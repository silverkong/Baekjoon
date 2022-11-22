def solution(N, stages):
    answer = []
    clear = {i : 0 for i in range(1, N + 2)}
    fail = {i : 0 for i in range(1, N + 2)}
    person = len(stages)
    
    for stage in stages:
        clear[stage] += 1
    
    for key, value in clear.items():
        if person != 0:
            temp = value / person
            fail[key] = temp
            person -= value
        else:
            fail[key] = 0
        
    fail.popitem()
    fail = dict(sorted(fail.items(), key=lambda x: x[1], reverse=True))
    
    for key in fail.keys():
        answer.append(key)
    
    return answer