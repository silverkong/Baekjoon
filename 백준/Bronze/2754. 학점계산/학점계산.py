s = list(input())

d = {'A' : 4.0, 'B' : 3.0, 'C' : 2.0, 'D' : 1.0, 'F' : 0.0, '+' : 0.3, '0' : 0.0, '-' : -0.3}

if len(s) == 2:
    print(d[s[0]] + d[s[1]])
else:
    print(d[s[0]])