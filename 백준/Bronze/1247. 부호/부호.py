import sys
for i in range(3):
    n = int(sys.stdin.readline())
    r = []
    for j in range(n):
        r.append(int(sys.stdin.readline()))
    if sum(r) == 0:
        print("0")
    elif sum(r) > 0:
        print("+")
    else:
        print("-")