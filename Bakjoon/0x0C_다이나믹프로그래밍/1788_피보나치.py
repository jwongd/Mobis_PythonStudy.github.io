N = int(input())
M = -1*N
dp = [0]*10000001

dp[0] = 0
dp[1] = 1
dp[2] = 1

for i in range(1,1000001):
    dp[i+2] = (dp[i] + dp[i+1])%1000000000
if N>0 :
    print(1)
    print(dp[N])
elif N == 0 :
    print(0)
    print(0)
else:
    if (-1*N) % 2 == 0:
        print(-1)
        print(dp[M])
    else:
        print(1)
        print(dp[M])