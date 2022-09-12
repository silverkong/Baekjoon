b = [1, 1, 2, 2, 2, 8]
w = list(map(int, input().split()))

for i in range(len(b)):
    if b[i] == w[i]:
        w[i] = 0
    else:
        if w[i] == 0:
            w[i] = b[i]
        else:
            w[i] = b[i] - w[i]

for i in range(len(w)):
    print(w[i], end=' ')
        