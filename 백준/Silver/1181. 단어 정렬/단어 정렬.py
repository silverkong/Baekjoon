n = int(input())

w = []
for i in range(n):
    w.append(input())
    
set_w = list(set(w))

sort_w = []
for i in set_w:
    sort_w.append((len(i), i))

r = sorted(sort_w)

for len_w, w in r:
    print(w)