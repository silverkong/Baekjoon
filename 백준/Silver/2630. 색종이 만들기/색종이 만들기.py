import sys

def color(x, y, n):
    global w, b
    check = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != paper[i][j]:
                color(x, y, n//2)
                color(x, y + n//2, n//2)
                color(x + n//2, y, n//2)
                color(x + n//2, y + n//2, n//2)
                return
              
    if check == 0:
        w += 1
        return
    else:
        b += 1
        return
N = int(input())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
w, b = 0, 0

color(0, 0, N)
print(w)
print(b)