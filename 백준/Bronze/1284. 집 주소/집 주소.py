r = []
while True:
    s = 0
    n = list(map(int, input()))
    if n[0] == 0:
        break
    for i in range(len(n)):
        if n[i] == 1:
            s += 2
        elif n[i] == 0:
            s += 4
        else:
            s += 3
    s += (len(n)+1)
    r.append(s)
    
for i in range(len(r)):
    print(r[i])