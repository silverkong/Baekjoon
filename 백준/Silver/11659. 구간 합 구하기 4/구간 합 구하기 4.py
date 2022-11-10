import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
sumNum = [0 for _ in range(N)]

for i in range(N):
    if i == 0:
        sumNum[i] = num[i]
    else:
        sumNum[i] = sumNum[i-1] + num[i]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i == 1:
        print(sumNum[j-1])
    else:
        print(sumNum[j-1] - sumNum[i-2])