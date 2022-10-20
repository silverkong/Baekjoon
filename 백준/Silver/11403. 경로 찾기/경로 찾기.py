import sys
INF = int(1e9)

N = int(sys.stdin.readline())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    a = list(map(int, sys.stdin.readline().split()))
    for j in range(len(a)):
        if a[j] == 1:
            graph[i][j+1] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()