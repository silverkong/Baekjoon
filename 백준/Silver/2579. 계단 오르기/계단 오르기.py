# 계단의 개수 입력 받기
N = int(input())
# 계단 점수 배열로 입력 받기
stairs = [int(input()) for _ in range(N)]

# 계단의 개수까지 0으로 초기화
dp = [0 for _ in range(N)]

# 계단이 2개 이하 일 경우에는 리스트의 합이 결과
if N <= 2:
    print(sum(stairs))
else:
    # dp[0] = 첫 번째 계단의 값
    dp[0] = stairs[0]
    # dp[1] = 두 번째 계단까지의 값
    dp[1] = stairs[0] + stairs[1]
    # dp[2] = 두 번째 계단을 밟고 한 계단 올랐을 때와 첫 번째 계단을 밟고 두 계단 올랐을 때 중 큰 값
    dp[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])
    # 마지막 계단을 꼭 밟아야 함
    # 마지막 전 단계 계단 밟았을 때와 마지막 전 단계 계단을 밟지 않았을 때 중 큰 값
    for i in range(3, N):
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])
    
    print(dp[N - 1])