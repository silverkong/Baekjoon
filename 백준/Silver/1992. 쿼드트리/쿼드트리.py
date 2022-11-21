import sys

def checkTree(x, y, n):
    global result
    check = quadTree[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != quadTree[i][j]:
                result += '('
                checkTree(x, y, n//2)
                checkTree(x, y + n//2, n//2)
                checkTree(x + n//2, y, n//2)
                checkTree(x + n//2, y + n//2, n//2)
                result += ')'
                return
              
    if check == 0:
        result += '0'
        return
    else:
        result += '1'
        return
N = int(input())
quadTree = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
result = ''

checkTree(0, 0, N)
print(result)