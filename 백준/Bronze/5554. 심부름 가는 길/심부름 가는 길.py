r = []
t = 0
for i in range(4):
    r.append(int(input()))
    t += r[i]
x = t//60
y = t%60
print(x)
print(y)