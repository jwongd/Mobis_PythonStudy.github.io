import sys
input = sys.stdin.readline
N = int(input())
INF = 1e9
dp = [INF]*100001
sq = [0]*317
for i in range(1,317):
    dp[i*i] = 1
    sq[i] = i*i
for i in range(2,N+1):
    if dp[i] == INF :
        for n in sq:
            if i - n >0 :
                dp[i] = min(dp[n] + dp[i-n],dp[i])
print(dp[N])

#################모범 답안#######################
n  = int(input())
dp = [0 for i in range(n+1)]
sq = [i*i for i in range(1,317)]
for i in  range(1,n+1):
    s = []
    for j in sq:
        if j > i:
            break
        s.append(dp[i-j])
    dp[i] = min(s)+1
print(dp[n])

#j는 i보다 작거나 같은 제곱수 , 이 때 i-j들의 목록 중 가장 작은 녀석에서 +1한게 답
# 즉 dp[i] =   min(dp[i-j])+1