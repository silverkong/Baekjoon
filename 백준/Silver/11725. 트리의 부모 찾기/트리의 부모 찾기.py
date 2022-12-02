import sys
sys.setrecursionlimit(1000000)

def dfs(v):
    for i in graph[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(i)

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)

dfs(1)

for i in range(2, N + 1):
    print(visited[i])