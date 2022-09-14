t = int(input())
r = []
c = 1
for i in range(t):
    a, b = map(int, input().split())
    r.append(a)
    r.append(b)
for i in range(0, len(r), 2):
    print("Case #", c, ": ", r[i], " + ", r[i+1], " = ", r[i]+r[i+1], sep='')
    c += 1