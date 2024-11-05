n = int(input())
for  _ in range(n):
    x = int(input())
    dp = [0] * (x+1)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 3
    dp[4] =  