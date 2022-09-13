s = list(input())
c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
r = [-1 for i in range(len(c))]
for i in range(len(s)):
    for j in range(len(c)):
        if ord(s[i]) == ord(c[j]) and r[j] == -1:
            r[j] = i
for i in range(len(r)):
    print(r[i], end=' ')