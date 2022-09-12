a = []
for i in range(1, 31):
    a.append(int(i))

for i in range(len(a)-2):
    a.remove(int(input()))

for i in range(len(a)):
    print(a[i])