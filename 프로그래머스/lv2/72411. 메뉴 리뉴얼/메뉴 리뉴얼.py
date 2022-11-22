from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    # [2,3,4]라면 2개 중 가장 많이 선택된 것, .. 을 진행하기 위해
    for c in course:
        # 조합을 담을 리스트 생성
        temp = []
        for order in orders:
            # 조합 찾기, sorted는 'A','C'와 'C','A'가 다르게 나올 수 있으므로 진행
            combi = combinations(sorted(order), c)
            # 조합을 모두 리스트에 담기
            temp += combi
        # 담은 조합을 카운팅
        counter = Counter(temp)
        # 만약 카운터의 길이가 0이 아니고 값의 최대 값이 1이 아니라면(2명 이상의 손님이 주문한 조합 선택)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)