import sys
INF = int(1e9)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

count = 0
for a in range(1, N + 1):
    if graph[1][a] != INF and graph[1][a] != 0:
        count += 1

print(count)