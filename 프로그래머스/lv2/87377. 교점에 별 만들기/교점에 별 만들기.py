from itertools import combinations

def calculation(eq1, eq2):
    x1, y1, c1 = eq1
    x2, y2, c2 = eq2
    
    if x1*y2 == y1*x2: 
        return
    
    x = (y1*c2-c1*y2)/(x1*y2-y1*x2)
    y = (c1*x2-x1*c2)/(x1*y2-y1*x2)
    
    if x == int(x) and y == int(y):
        return [int(x), int(y)]

def solution(lines):
    points = []
    for eq1, eq2 in combinations(lines,2):
        point = calculation(eq1,eq2)
        if point: points.append(point)
        
    w1, w2 = min(points, key = lambda x : x[0])[0], max(points, key = lambda x : x[0])[0] + 1
    h1, h2 = min(points, key = lambda x : x[1])[1], max(points, key = lambda x : x[1])[1] + 1
    
    answer = [['.'] * (w2 - w1) for _ in range((h2 - h1))]

    for x, y in points:
        answer[y-h1][x-w1] = '*'
    
    answer.reverse()
    
    return [''.join(a) for a in answer]