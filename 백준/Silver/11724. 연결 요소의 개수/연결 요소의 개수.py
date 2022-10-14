from collections import deque
import sys

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M = map(int, sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
count = 0
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] + [False] * (N)

for i in range(1, len(visited)):
    if visited[i] == False:
        count += 1
        bfs(graph, i, visited)

print(count)