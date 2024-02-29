N = int(input())
#선공이 이기면 1, 지면 0으로 설정
dp = [0]*(N+1)
dp[1] = 1
if N >=2:
    dp[2] = 0
if N >=3:
    dp[3] = 1
if N >=4:
    dp[4] = 1
for i in range(5,N+1):
    if dp[i-1] == 1 and dp[i-3] == 1 and dp[i-4] == 1:
        dp[i] = 0
    else:
        dp[i] = 1
if dp[N] == 1:
    print("SK")
else:
    print("CY")