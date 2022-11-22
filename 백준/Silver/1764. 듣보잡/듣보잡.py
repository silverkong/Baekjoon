import sys

N, M = map(int, input().split())
neverHeard = {}
neverHeardSeen = {}
count = 0

for _ in range(N):
    temp = sys.stdin.readline().rstrip()
    neverHeard[temp] = 1

for _ in range(M):
    temp = sys.stdin.readline().rstrip()
    if temp in neverHeard:
        count += 1
        neverHeardSeen[temp] = 1

neverHeardSeen = dict(sorted(neverHeardSeen.items()))
print(count)
for key, value in neverHeardSeen.items():
    print(key)