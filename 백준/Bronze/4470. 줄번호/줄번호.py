n = int(input())
r = []
for i in range(n):
    r.append(input())
for i in range(len(r)):
    print(i+1, '. ', r[i], sep='')