import sys

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        return 1
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

N = int(sys.stdin.readline())
NA = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
MA = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    result = binary_search(NA, MA[i], 0, N-1)
    print(result)