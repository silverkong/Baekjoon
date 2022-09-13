t = int(input())
a = []
for i in range(t):
    a.append(list(input()))

for i in range(t):
    if len(a[i]) == 1:
        print(a[i][0], end='')
        print(a[i][0], end='')
    else:
        print(a[i][0], end='')
        print(a[i][len(a[i])-1], end='')  
    print()