def solution(n, words):
    answer = []
    count = dict()

    for i in range(len(words)):
        if words[i] in count:
            answer = [(i % n) + 1, (i // n) + 1]
            break
        
        if i != 0 and words[i - 1][-1:] != words[i][:1]:
            answer = [(i % n) + 1, (i // n) + 1]
            break
        
        count[words[i]] = 1
    
    if len(answer) == 0:
        answer = [0, 0]

    return answer