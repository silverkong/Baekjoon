from bisect import bisect_left, bisect_right
import sys

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array,left_value)
    return right_index - left_index

N = int(sys.stdin.readline())
NA = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
MA = list(map(int, sys.stdin.readline().split()))
R = [0] * M

for i in range(M):
    count = count_by_range(NA, MA[i], MA[i])
    R[i] = count

print(*R, sep=' ')