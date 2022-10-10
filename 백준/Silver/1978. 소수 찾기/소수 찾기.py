n = int(input())
nums = map(int, input().split())
r = 0
for i in nums:
    no = 0
    if i > 1 :
        for j in range(2, i):
            if i % j == 0:
                no += 1
        if no == 0:
            r += 1
print(r)