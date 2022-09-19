p, k = map(int, input().split())
a = True
for i in range(2, k):
    if p % i == 0:
        print('BAD', i)
        a = False
        break
if a:
      print('GOOD')