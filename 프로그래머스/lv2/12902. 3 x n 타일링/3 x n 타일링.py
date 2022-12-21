def solution(n):    
    if n % 2 != 0:
        return 0
    else:
        tiles = [0 for _ in range(5001)]
        tiles[0] = 1
        tiles[2] = 3
        
        for i in range(4, n + 1, 2):
            tiles[i] = (tiles[i - 2] * 3)
            for j in range(i - 4, -1, -2):
                tiles[i] += (tiles[j] * 2)
            tiles[i] %= 1000000007
        
        return tiles[n]
    