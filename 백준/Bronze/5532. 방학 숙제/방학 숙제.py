import math
l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

k = math.ceil(a/c)
m = math.ceil(b/d)

if k > m:
    print(l - k)
else:
    print(l - m)