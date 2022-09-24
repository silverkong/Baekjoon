t = int(input())
r = []

for i in range(t):
    n, m = map(int, input().split())
    num1 = 1
    num2 = 1
    num3 = 1
    for j in range(1, n+1):
        num1 *= j
    for j in range(1, m+1):
        num2 *= j
    for j in range(1, (m-n)+1):
        num3 *= j
    result = num2//(num1*num3)
    r.append(result)
    
for i in range(len(r)):
    print(r[i])