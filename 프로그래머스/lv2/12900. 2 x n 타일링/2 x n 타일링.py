def solution(n):
    tiles = [0 for _ in range(60001)]
    tiles[1] = 1
    tiles[2] = 2
    
    for i in range(3, n + 1):
        tiles[i] = (tiles[i - 1] + tiles[i - 2]) % 1000000007
    
    return tiles[n]