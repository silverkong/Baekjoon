def solution(n, lost, reserve):
    setLost = set(lost) - set(reserve)
    setReserve = set(reserve) - set(lost)
        
    for r in setReserve:
        if r - 1 in setLost:
            setLost.remove(r - 1)
        elif r + 1 in setLost:
            setLost.remove(r + 1)
    
    answer = n - len(setLost)
    
    return answer