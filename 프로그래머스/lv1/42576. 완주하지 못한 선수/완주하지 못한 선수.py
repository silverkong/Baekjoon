def solution(participant, completion):
    answer = ''
    names = {}
    sumHash = 0
    
    for part in participant:
        names[hash(part)] = part
        sumHash += hash(part)
    
    for comp in completion:
        sumHash -= hash(comp)
    
    answer = names[sumHash]
    
    return answer