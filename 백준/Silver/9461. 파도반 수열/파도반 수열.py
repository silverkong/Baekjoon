result = [0 for _ in range(101)]
result[1], result[2], result[3] = 1, 1, 1
for i in range(4, len(result)):
    result[i] = result[i - 3] + result[i - 2]

T = int(input())

for _ in range(T):
    N = int(input())
    print(result[N])