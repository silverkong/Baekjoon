t = int(input())
r = []
for i in range(t):
    a, b = map(int, input().split())
    r.append(a+b)
for i in range(len(r)):
    print("Case #", end='')
    print(i+1, end='')
    print(":", end=' ')
    print(r[i])