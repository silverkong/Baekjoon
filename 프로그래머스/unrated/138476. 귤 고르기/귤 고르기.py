from collections import Counter
from operator import itemgetter

def solution(k, tangerine):
    answer = 0
    tangerineCount = Counter(tangerine)
    calc = k
    tangerineCount = dict(sorted(tangerineCount.items(), key=lambda x: (-x[1], x[0])))

    for key, value in tangerineCount.items():
        calc -= value
        answer += 1
        if calc <= 0:
            break
    
    return answer