def solution(n, words):
    answer = []
    count = dict()

    for i in range(len(words)):
        if words[i] in count:
            no = (i % n) + 1
            order = (i // n) + 1
            answer = [no, order]
            break
        
        if i != 0 and words[i - 1][-1:] != words[i][:1]:
            no = (i % n) + 1
            order = (i // n) + 1
            answer = [no, order]
            break
        
        count[words[i]] = 1
    
    if len(answer) == 0:
        answer = [0, 0]

    return answer