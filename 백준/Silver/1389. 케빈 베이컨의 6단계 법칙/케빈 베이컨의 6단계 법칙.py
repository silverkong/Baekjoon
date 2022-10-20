import sys
INF = int(1e9)

N, M = map(int, sys.stdin.readline().split())
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

result = []
for a in range(1, N + 1):
    tmp = 0
    for b in range(1, N + 1):
        tmp += graph[a][b]
    result.append(tmp)

print(result.index(min(result)) + 1)