from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]

for _ in range(M):
    X, Y = map(int, input().split())
    graph[X].append(Y)
    graph[Y].append(X)
    graph[X].sort()
    graph[Y].sort()

visited = [False] * (N+1)
dfs(graph, V, visited)
print()

visited = [False] * (N+1)
bfs(graph, V, visited)