def solution(nums):
    answer = 0
    numsDict = {}
    pokemon = []
    
    for i in nums:
        if i in numsDict:
            numsDict[i] += 1
        else:
            numsDict[i] = 1
    
    print(numsDict)
    
    for key, value in numsDict.items():
        if len(pokemon) == (len(nums) // 2):
            break
            
        if key in pokemon:
            continue
        else:
            answer += 1
            pokemon.append(key)
    
    return answer