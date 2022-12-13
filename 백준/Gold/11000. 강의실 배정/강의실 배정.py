import heapq
import sys

# 수업 개수
N = int(sys.stdin.readline())
# 수업 스케쥴
time = []

# N개 수업 입력 받기
for _ in range(N):
    # 시작, 끝 시간
    start, end = map(int, sys.stdin.readline().split())
    # 리스트 형태로 추가
    time.append([start, end])

time.sort()

last = []
heapq.heappush(last, time[0][1])

# 정렬된 수업 스케쥴 시작, 끝 시간 비교
for i in range(1, len(time)):
    # 수업 끝 시간보다 시작 시간이 빠르다면
    if time[i][0] < last[0]:
        heapq.heappush(last, time[i][1])
    else: # 아니라면
        # 가장 앞에 있는 시간 삭제
        heapq.heappop(last)
        # 현재 끝 시간 추가
        heapq.heappush(last, time[i][1])

print(len(last))