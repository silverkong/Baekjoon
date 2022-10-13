import sys

N = int(sys.stdin.readline())
A = []
for i in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))

A.sort()

for i in range(len(A)):
    print(A[i][0], A[i][1])