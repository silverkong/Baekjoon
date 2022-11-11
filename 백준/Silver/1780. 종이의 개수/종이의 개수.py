import sys

def cut(x, y, n):
    global a, b, c
    check = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                n1 = n//3
                n2 = n//3 * 2
                cut(x, y, n1)
                cut(x + n1, y, n1)
                cut(x + n2, y, n1)
                cut(x, y + n1, n1)
                cut(x + n1, y + n1, n1)
                cut(x + n2, y + n1, n1)
                cut(x, y + n2, n1)
                cut(x + n1, y + n2, n1)
                cut(x + n2, y + n2, n1)
                return
              
    if check == -1:
        a += 1
        return
    elif check == 0:
        b += 1
        return
    else:
        c += 1
        return
      
N = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

a, b, c = 0, 0, 0

cut(0, 0, N)
print(a)
print(b)
print(c)