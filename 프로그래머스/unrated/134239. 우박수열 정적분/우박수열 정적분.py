def solution(k, ranges):
    answer = []
    sequence = [k]
    area = []
    
    # 수열 구하기
    while k != 1:
        if k % 2 == 0:
            k = k // 2
        else:
            k = (k * 3) + 1
        sequence.append(k)
    
    # 넓이 구하기
    for i in range(len(sequence)):
        if sequence[i] == 1:
            break
        
        if sequence[i] % 2 == 0:
            area.append(((sequence[i] - sequence[i + 1]) / 2) + sequence[i + 1])
        else:
            area.append(sequence[i] + ((sequence[i + 1] - sequence[i]) / 2))
    
    for r in ranges:
        if r[0] == 0 and r[1] == 0:
            answer.append(sum(area))
        else:
            if r[0] > len(area) + r[1]:
                answer.append(-1.0)
            else:
                temp = 0.0
                for i in range(r[0], len(area) + r[1]):
                    temp += area[i]
                answer.append(temp)                
    
    return answer