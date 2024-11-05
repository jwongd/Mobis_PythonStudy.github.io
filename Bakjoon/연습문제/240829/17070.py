n = int(input())
graph = [] ; dp = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
dp = [[0]*(n+1) for _ in range(n+1)]
dp[0][0] = 1
dp[0][1] = 1
for i in range(n):
    for j in range(2,n):
        if graph[i][j] == 0 and graph[i][j-1] == 0:
            dp[i][j] += dp[i][j-2]
for i in range(2,n):
    for j in range(n):
        if graph[i][j] == 0 and graph[i-1][j] == 0:
            dp[i][j] += dp[i-2][j]
for i in range(1,n):
    for j in range(1,n) :
        if graph[i][j] == 0 and graph[i][j-1] == 0 and graph[i-1][j] == 0:
            dp[i][j] += dp[i-1][j-1]
for i in dp:
    print(*i)
ans = dp[n-1][n-1]
print(ans)