import math

def solution(arrayA, arrayB):
    answer = 0
    gcdArrA, gcdArrB = gcdF(arrayA), gcdF(arrayB)
    
    for i in arrayA:
        if i % gcdArrB == 0:
            break
    else:
        answer = max(gcdArrB, answer)
        
    for i in arrayB:
        if i % gcdArrA == 0:
            break
    else:
        answer = max(gcdArrA, answer)
    
    return answer
 
def gcdF(arr):
    gcdValue = arr[0]
    for i in range(1, len(arr)):
        gcdValue = math.gcd(gcdValue, arr[i])
        
    return gcdValue
