# 7569번 토마토
from collections import deque
import sys

# 이동할 6가지 방향 정의
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

# BFS 소스코드 구현
def bfs():
    # 큐가 빌 때까지 반복하기
    while queue:
        z, x, y = queue.popleft()
        # 현재 위치에서 6가지 방향으로의 위치 확인
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            # 박스 안에 있는 경우만 체크
            if -1 < nx < N and -1 < ny < M and -1 < nz < H:
                # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = box[z][x][y] + 1
                    queue.append((nz, nx, ny))

# M, N, H를 공백을 기준으로 입력 받기
M, N, H = map(int, sys.stdin.readline().split())

# 토마토 상자 만들기
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        for k in range(M):
           if box[i][j][k] == 1:
              queue.append((i, j, k))
bfs()
flag = 0
max_num = -2

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                flag = 1
            max_num = max(max_num, box[i][j][k])

if flag == 1:
    print(-1)
elif max_num == -1:
    print(0)
else:
    print(max_num - 1)