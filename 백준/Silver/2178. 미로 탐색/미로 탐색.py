from collections import deque
import sys

# 이동할 4가지 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

# BFS 소스코드 구현
def bfs(x, y):
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 박스 안에 있는 경우만 체크
            if -1 < nx < N and -1 < ny < M:
                # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx, ny))
    # N, M 위치 최단거리 반환
    return maze[N - 1][M - 1]

# N, M를 공백을 기준으로 입력 받기
N, M = map(int, sys.stdin.readline().split())

# 미로 만들기
maze = [list(map(int, input())) for _ in range(N)]

print(bfs(0, 0))