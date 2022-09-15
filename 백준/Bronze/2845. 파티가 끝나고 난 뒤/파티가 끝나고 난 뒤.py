l, p = map(int, input().split())
a = list(map(int, input().split()))
r = []
for i in range(len(a)):
    r.append(a[i] - l*p)
for i in range(len(r)):
    print(r[i], end=' ')