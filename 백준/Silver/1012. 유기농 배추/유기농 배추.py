# 1012번 유기농 배추
# 재귀한도 해제
import sys
sys.setrecursionlimit(10000)

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 해당 노드 방문 처리
        graph[x][y] = 0
        # 상, 하, 좌, 우의 위치들도 모드 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 테스트 케이스의 개수 입력 받기
T = int(input())
# 테스트 케이스만큼 반복
for _ in range(T):
    # M, N, K를 공백을 기준으로 입력 받기
    M, N, K = map(int, input().split())

    # 배추가 하나도 심어져 있지 않은 밭 그리기
    graph = [[0 for i in range(M)] for i in range(N)]
    # K번 만큼 배추 심기
    for _ in range(K):
        # 배추의 위치를 공백을 기준으로 입력 받기
        x, y = map(int, input().split())
        graph[y][x] = 1

    # 모든 위치를 돌며 필요한 지렁이 수 확인하기
    result = 0
    for i in range(N):
        for j in range(M):
            # 현재 위치에서 DFS 수행
            if dfs(i, j) == True:
                result += 1
    print(result)