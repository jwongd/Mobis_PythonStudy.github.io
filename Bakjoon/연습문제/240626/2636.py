from collections import deque
dx = [-1,1,0,0] ; dy = [0,0,-1,1]
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
def bfs(a,b):
    q = deque()
    q.append((a,b))
    vis[a][b] = 1
    while q:
        x,y = q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir] , y + dy[dir]
            if 0<=nx<n and 0<=ny<m and not vis[nx][ny] :
                if graph[nx][ny] == 0:
                    q.append((nx,ny))
                    vis[nx][ny] = 1
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    vis[nx][ny] = 1
s = 1
ans = []
ans.append(sum(map(sum,graph)))
#print(ans)
while s:
    vis = [[0]*m for _ in range(n)]
    bfs(0,0)
    cnt += 1
    s = sum(map(sum, graph))
    if s != 0:
        ans.append(s)
print(cnt)
print(ans[-1])