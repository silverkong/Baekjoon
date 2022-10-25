N, M = map(int, input().split())
chess = []
count = []
  
for _ in range(N):
    chess.append(input())

for i in range(N - 7):
    for j in range(M - 7): # 8X8 체스판 인덱스 벗어나지 않기 위함
        chk1 = 0
        chk2 = 0
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if chess[a][b] != 'B':
                        chk1 += 1
                    if chess[a][b] != 'W':
                        chk2 += 1
                else:
                    if chess[a][b] != 'W':
                        chk1 += 1
                    if chess[a][b] != 'B':
                        chk2 += 1
        count.append(chk1)
        count.append(chk2)

print(min(count))