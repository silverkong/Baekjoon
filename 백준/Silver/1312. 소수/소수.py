a, b, n = map(int, input().split(' '))

a = a % b
for i in range(n - 1):
    a = (a * 10) % b

r = (a * 10) // b
print(r)