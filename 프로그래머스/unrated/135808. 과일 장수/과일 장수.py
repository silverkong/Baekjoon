def solution(k, m, score):
    answer = 0
    score.sort()
    for packed in range(len(score),m-1, -m):
        answer += score[packed-m]*m
        
    return answer