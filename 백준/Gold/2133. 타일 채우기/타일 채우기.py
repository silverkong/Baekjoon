N = int(input())
if N % 2 != 0:
    print(0)
else:
    calArr = [0 for _ in range(31)]
    calArr[0] = 1
    calArr[2] = 3
    
    for i in range(4, N + 1, 2):
        calArr[i] = calArr[i - 2] * 3
        for j in range(i - 4, -1, -2):
            calArr[i] += calArr[j] * 2
    
    print(calArr[N])