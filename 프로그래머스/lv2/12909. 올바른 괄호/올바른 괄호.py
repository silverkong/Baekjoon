from collections import deque
def solution(s):
    bracket = []
    
    for b in s:
        if b == '(':
            bracket.append(b)
        else:
            if '(' in bracket:
                bracket.pop()
            else:
                return False
    if len(bracket) != 0:
        return False

    return True