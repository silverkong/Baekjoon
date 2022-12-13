from collections import Counter

def solution(want, number, discount):
    answer = 0
    wtCount = {}
    
    for i in range(len(want)):
        wtCount[want[i]] = number[i]
    
    for i in range(len(discount) - 9):
        dcCut = discount[i : i + 10]
        dcCount = Counter(dcCut)
        if dcCount == wtCount:
            answer += 1
    
    return answer