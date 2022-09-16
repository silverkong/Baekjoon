n = int(input())
c = list(map(int, input().split()))
y, m = 0, 0
for i in range(len(c)):
    y += 10 + (10 * (c[i]//30))
    m += 15 + (15 * (c[i]//60))
if y < m:
    print('Y', y)
elif y > m:
    print('M', m)
else:
    print('Y', 'M', y)