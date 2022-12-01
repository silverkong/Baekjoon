from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        x = q.popleft()
        for dice in range(1, 7):
            move = x + dice
            if move <= 100 and not visited[move] == True:
                if move in ladder.keys():
                    move = ladder[move]
                if move in snake.keys():
                    move = snake[move]
                if not visited[move] == True:
                    q.append(move)
                    visited[move] = True
                    board[move] = board[x] + 1
                if move == 100:
                    q = []
                    break

N, M = map(int, input().split())
ladder = {}
snake = {}
board = [0] * 101
visited = [False] * 101

for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(M):
    x, y = map(int, input().split())
    snake[x] = y

bfs(1)
print(board[100])