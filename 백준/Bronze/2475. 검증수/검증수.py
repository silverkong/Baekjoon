a = input().split()
r = 0
for i in range(5):
    a[i] = int(a[i])
for i in range(5):
    r += (a[i]**2)
print(r%10)