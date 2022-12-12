from itertools import permutations

def solution(k, dungeons):
    hp = k
    count = []
    arr = list(permutations(dungeons))

    for a in arr:
        temp = 0
        for x, y in a:
            if x <= hp:
                hp -= y
                temp += 1
            else:
                break
        count.append(temp)
        if temp == len(dungeons):
            break
        hp = k
        
    answer = max(count)
    return answer