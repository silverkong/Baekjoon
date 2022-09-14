a, b, c = map(int, input().split())
r = [a, b, c]
temp = 0
for i in range(len(r)-1):
    for j in range(i+1, len(r)):
        if r[i] > r[j]:
            temp = r[i]
            r[i] = r[j]
            r[j] = temp
for i in range(len(r)):
    print(r[i], end=' ')