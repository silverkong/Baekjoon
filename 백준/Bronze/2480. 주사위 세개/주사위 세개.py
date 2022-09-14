a = list(map(int, input().split()))
c = 0
s = 0
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            c += 1
            s = a[i]
if c == 0:
    b = 0
    for i in range(len(a)):
        if b < a[i]:
            b = a[i]
    print(b*100)
elif c == 1:
    print(1000+s*100)
else:
    print(10000+s*1000)