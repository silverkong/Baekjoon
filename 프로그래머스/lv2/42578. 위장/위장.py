def solution(clothes):
    answer = 1
    clothesHash = {}
    
    for cloth in clothes:
        if cloth[1] not in clothesHash.keys():
            clothesHash[cloth[1]] = 1
        else:
            clothesHash[cloth[1]] += 1
            
    for key, value in clothesHash.items():
        answer *= (value + 1)
    
    answer -= 1
    
    return answer