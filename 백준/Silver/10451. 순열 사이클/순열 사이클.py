from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

T = int(input())
count = []
for _ in range(T):
    N = int(input())
    figure = list(map(int, input().split()))
    graph = [[] for i in range(N+1)]
    countTemp = 0
    for i in range(1, len(figure)+1):
        graph[i].append(figure[i-1])
        graph[figure[i-1]].append(i)
    visited = [False] * (N + 1)
    for i in range(1, len(visited)):
        if visited[i] == False:
            countTemp += 1
            bfs(graph, i, visited)
    count.append(countTemp)

print(*count, sep='\n')