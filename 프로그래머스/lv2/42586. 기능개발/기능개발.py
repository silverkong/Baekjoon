from collections import deque

def solution(progresses, speeds):
    ProgressesQue = deque(progresses)
    SpeedsQue = deque(speeds)
    count = 0
    answer = []
    while ProgressesQue:
        if ProgressesQue[0] + SpeedsQue[0] >= 100:
            ProgressesQue.popleft()
            SpeedsQue.popleft()
            count += 1
        else:
            if count:
                answer.append(count)
                count = 0
            for i in range(len(ProgressesQue)):
                ProgressesQue[i] += SpeedsQue[i]
    answer.append(count)
    return answer