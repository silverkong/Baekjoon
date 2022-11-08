# 1927번 최소 힙
import heapq
import sys

N = int(input())
arr = []
for _ in range(N):
    X = int(sys.stdin.readline())
    if X != 0:
        heapq.heappush(arr, X)
    else:
        if len(arr) != 0:
            print(heapq.heappop(arr))
        else:
            print(0)