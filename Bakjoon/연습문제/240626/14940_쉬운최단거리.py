from collections import deque
dx = [-1,1,0,0] ; dy = [0,0,-1,1]
n , m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
q = deque()
vis = [[-1]*(m) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            q.append((i,j))
            vis[i][j] = 0


for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            vis[i][j] = 0
while q:
    x , y = q.popleft()
    for dir in range(4):
        nx , ny = x + dx[dir], y+dy[dir]
        if 0<=nx < n and 0<=ny < m and graph[nx][ny] == 1 :
            if vis[nx][ny] == -1:
                vis[nx][ny] = vis[x][y] + 1
                q.append((nx,ny))
for i in vis:
    print(*i)
