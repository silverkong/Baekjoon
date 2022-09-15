r = []
for i in range(5):
    r.append(int(input()))
H = r[0]
for i in range(3):
    if r[i] < H:
        H = r[i]
if r[3] < r[4]:
    B = r[3]
else:
    B = r[4]
print(H+B-50)
        