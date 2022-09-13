n = int(input())
a = [0 for i in range(n)]
a = list(map(int, input().split()))
v = int(input())
c = 0
for i in range(len(a)):
    if a[i] == v:
        c += 1
print(c)