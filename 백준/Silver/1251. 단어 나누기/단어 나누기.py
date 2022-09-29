s = list(input())
r = []
t = []

for i in range(1, len(s) - 1):
    for j in range(i + 1, len(s) ):
        a = s[:i]
        b = s[i:j]
        c = s[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        t.append(a + b + c)

for a in t:
    r.append(''.join(a))

print(sorted(r)[0])