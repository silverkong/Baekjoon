import sys
from collections import deque

# 테스트 케이스 개수
T = int(input())
# 테스트 케이스만큼 반복
for _ in range(T):
    # 수행할 함수
    p = input()
    # 배열에 들어간 수의 개수
    n = int(input())
    # 배열에 들어 있는 정수 리스트 받고 양 옆의 '[', ']' 자르기
    x = sys.stdin.readline().rstrip()[1:-1].split(',')

    # 큐에 리스트 넣어주기
    queue = deque(x)
    # n이 0이라면 빈 큐로 초기화(길이가 1인 큐)
    if n == 0:
        queue = []

    # 상태 표기 위한 변수들 선언
    flag = 0
    rCount = 0

    # 함수 수행
    for i in p:
        if i == 'R':
            rCount += 1
        else:
            if len(queue) == 0:
                flag = 1
                print('error')
                break
            else: # deque의 경우 양방향으로 pop 가능
                if rCount % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    # flag가 1이면 에러이므로 0일 경우만 출력
    if flag == 0:
        if rCount % 2 == 0:
            print("[", ','.join(queue), ']', sep='')
        else:
            queue.reverse()
            print("[", ','.join(queue), ']', sep='')