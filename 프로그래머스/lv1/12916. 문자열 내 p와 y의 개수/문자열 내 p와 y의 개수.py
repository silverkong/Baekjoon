def solution(s):
    answer = True
    s = s.lower()
    pCount = 0
    yCount = 0
    
    if 'p' not in s and 'y' not in s:
        return True
    else:
        for a in s:
            if a == 'p':
                pCount += 1
            elif a == 'y':
                yCount += 1
        if pCount == yCount:
            return True
        else:
            return False