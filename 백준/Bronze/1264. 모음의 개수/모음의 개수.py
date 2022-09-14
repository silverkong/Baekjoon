r = []
v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    s = list(input())
    if s[0] == '#':
        break
    c = 0
    for i in range(len(s)):
        for j in range(len(v)):
            if s[i] == v[j]:
                c += 1
    r.append(c)
for i in range(len(r)):
    print(r[i])