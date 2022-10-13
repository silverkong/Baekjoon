import sys
input = sys.stdin.readline

N = int(sys.stdin.readline())
A = []
for i in range(N):
    A.append(int(input()))

print(*sorted(A), sep='\n')