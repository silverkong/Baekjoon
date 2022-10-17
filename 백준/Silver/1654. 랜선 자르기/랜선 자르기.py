import sys

K, N = map(int, sys.stdin.readline().split())
array = []
for i in range(K):
    array.append(int(sys.stdin.readline()))

start = 1
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        total += x//mid
    if total < N:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)