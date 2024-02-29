N,M = map(int,input().split())
board = []
for i in range(N):
    board.append(list(map(int,input().split())))
dp = [[0]*(M+1) for _ in range(N+1)]
dp[0][0] = board[0][0]
for i in range(1,M):
    dp[0][i] = dp[0][i-1] + board[0][i]
for i in range(1,N):
    dp[i][0] = dp[i-1][0] + board[i][0]
for i in range(2,N+1):
    for j in range(2,M+1):
        dp[i-1][j-1] = board[i-1][j-1] + max(dp[i-2][j-2],dp[i-1][j-2],dp[i-2][j-1])
print(dp[N-1][M-1])