import sys

N = int(input())
xList = list(map(int, sys.stdin.readline().split()))
result = sorted(list(set(xList)))

dic = {result[i] : i for i in range(len(result))}

for i in xList:
    print(dic[i], end=' ')