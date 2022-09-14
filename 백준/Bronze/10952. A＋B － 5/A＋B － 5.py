r = []
while True:
    a, b = map(int, input().split())
    if a+b == 0:
        break
    r.append(a+b)
for i in range(len(r)):
    print(r[i])