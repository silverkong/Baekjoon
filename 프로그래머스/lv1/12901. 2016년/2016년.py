def solution(a, b):
    day = ("FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU")
    month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    
    count = -1
    
    for i in range(a - 1):
        count += month[i]
    
    return day[(count + b) % 7]