from collections import deque
n,m = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
vis = [[[0]*2 for _ in range(m)] for _ in range(n)]
vis[0][0][0] = 1
q = deque()
def bfs(a,b,c):
    q.append((a,b,c))
    while q:
        x,y,z = q.popleft()
        if x == n-1 and y == m-1 :
            return vis[x][y][z]
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            nz = z
            if 0<= nx < n and 0<= ny < m :
            # case 1 : 일반적인 경우
                if graph[nx][ny] == 0 and vis[nx][ny][nz] == 0:
                    vis[nx][ny][nz] =  vis[x][y][nz] + 1
                    q.append((nx,ny,nz))
            # case 2: 벽 뚫을 수 있고, 벽일때
                if graph[nx][ny] == 1 and nz == 0:
                    vis[nx][ny][1] = vis[x][y][0] + 1
                    q.append((nx,ny,1))
    return -1
print(bfs(0,0,0))