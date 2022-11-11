import sys

def cut(x, y, n):
    global a, b, c
    check = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != paper[i][j]:
                cut(x, y, n//3)
                cut(x + n//3, y, n//3)
                cut(x + (n//3 * 2), y, n//3)
                cut(x, y + n//3, n//3)
                cut(x + n//3, y + n//3, n//3)
                cut(x + (n//3 * 2), y + n//3, n//3)
                cut(x, y + (n//3 * 2), n//3)
                cut(x + n//3, y + (n//3 * 2), n//3)
                cut(x + (n//3 * 2), y + (n//3 * 2), n//3)
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