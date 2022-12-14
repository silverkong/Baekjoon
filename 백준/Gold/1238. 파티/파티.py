import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

# N개의 마을, M개의 단방향 도로, X번 마을에 모여서 파티
N, M, X = map(int, input().split())
# 노드 리스트
graph = [[] for _ in range(N + 1)]
# 최단거리 무한으로 초기화
distance = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
# 왕복거리 담을 리스트
result = [0 for _ in range(N + 1)]

# 도로의 시작점, 끝점, 소요시간
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작점으로 가는 최단거리 = 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start][start] = 0
    # 큐가 비어있지 않다면
    while q:
        dist, now = heapq.heappop(q)
        if distance[start][now] < dist:
            continue
        # 연결된 도로 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[start][i[0]]:
                distance[start][i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

for i in range(1, N + 1):
    dijkstra(i)

for i in range(1, N + 1):
    result[i] = distance[i][X] + distance[X][i]

print(max(result))