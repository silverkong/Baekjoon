n, k = map(int, input().split())
a = []

for i in range(n):
    a.append(int(input()))
a.reverse()

r = 0
for i in a:
    if k == 0:
        break
    r += k//i
    k %= i

print(r)