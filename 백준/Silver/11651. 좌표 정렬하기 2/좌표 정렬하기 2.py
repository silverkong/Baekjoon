N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

A.sort(key=lambda x: (x[1], x[0]))

for i in range(len(A)):
    print(A[i][0], A[i][1])