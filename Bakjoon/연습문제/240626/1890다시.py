from collections import deque
dx = [1,0] ; dy = [0,1]
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]
q = deque()
q.append((0,0))
dp[0][0] = 0
while q:
    x,y = q.popleft()
    val = graph[x][y]
    #print("val",val)
    for dir in range(2):
        nx,ny = x + val*dx[dir] , y +dy[dir]*val
        #print("nx:",nx,"ny:",ny)
        if 0<=nx<n and 0<=ny<n and dp[nx][ny] == -1:
            dp[nx][ny] = dp[x][y] + 1
            q.append((nx,ny))
if dp[n-1][n-1] == -1:
    print(0)
else:
    print(dp[n-1][n-1])

# 9
# 3 1 2 2 3 3 1 1 2
# 1 1 2 1 1 2 3 1 2
# 2 1 1 3 2 2 1 3 1
# 3 3 1 1 1 3 1 2 1
# 3 2 2 2 1 1 3 3 1
# 3 1 3 2 2 3 1 3 3
# 3 1 1 2 1 1 1 1 1
# 2 3 1 3 1 3 2 2 2
# 3 3 3 2 3 1 3 3 0