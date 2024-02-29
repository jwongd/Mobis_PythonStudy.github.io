from collections import deque
n,m = map(int,input().split())
graph = []
# 3-dimension usage (vis[x][y][0] : destroy O , vis[x][y][1] : destroy x)
vis = [[[0]*2 for _ in range(m)] for _ in range(n)]
vis[0][0][0] = 1
for i in range(n):
    graph.append(list(map(int,input())))
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def bfs(a,b,c):
    q = deque()
    q.append((a,b,c))
    while q:
        x,y,z = q.popleft()
        if x == n-1 and y == m-1 :
            return vis[x][y][z]
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0<nx<=n and 0<ny<=m:
                # case 1 ) 다음 이동할 곳이 벽 + 벽 파괴 기회 남은 경우
                if graph[nx][ny] == 1 and z == 0:
                    vis[nx][ny][1] = vis[x][y][0] + 1
                    q.append((nx,ny,1))
                # case 2 ) 다음 이동할 곳이 벽이 아님 + 한 번도 방문 X (기존 bfs)
                elif graph[nx][ny] == 0 and vis[nx][ny][z] == 0:
                    vis[nx][ny][z] = vis[x][y][z] + 1
                    q.append((nx,ny,z))
    return -1
print(bfs(0,0,0))