import sys

N = int(sys.stdin.readline())
count = 0

count += N // 5
count += N // 25
count += N // 125

print(count)