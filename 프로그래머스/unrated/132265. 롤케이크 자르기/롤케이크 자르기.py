from collections import Counter

def solution(topping):
    answer = 0
    cake_top = Counter(topping)
    cake_top2 = set()
    
    for top in topping:
        cake_top[top] -= 1
        cake_top2.add(top)
        if cake_top[top] == 0:
            cake_top.pop(top)
        if len(cake_top) == len(cake_top2):
            answer += 1
            
    return answer