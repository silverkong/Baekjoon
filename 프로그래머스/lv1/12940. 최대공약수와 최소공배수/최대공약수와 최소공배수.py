import math

def solution(n, m):
    gcdNum = math.gcd(n, m)
    lcmNum = (n * m) // gcdNum
    
    return [gcdNum, lcmNum]