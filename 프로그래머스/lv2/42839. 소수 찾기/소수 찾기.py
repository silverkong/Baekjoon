from itertools import permutations

# 특정 숫자 x가 소수인지 판별하는 가장 기본적인 알고리즘
def primenumber(x):
    for i in range(2, x):	# 2부터 x-1까지의 모든 숫자
    	if x % i == 0:		# 나눠떨어지는게 하나라도 있으면 False
        	return False
    return True	

def solution(numbers):
    answer = 0
    numArray = list(map(int, numbers))
    arrPer = []
    
    for i in range(1, len(numArray) + 1):
        tempArray = list((permutations(numArray, i)))
        for j in range(len(tempArray)):
            arrPer.append(int(''.join(map(str, tempArray[j]))))
    
    arrPer = list(set(arrPer))
    
    for i in range(len(arrPer)):
        if arrPer[i] == 0 or arrPer[i] == 1:
            continue
            
        if primenumber(arrPer[i]):
            answer += 1
    
    return answer