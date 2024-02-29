from collections import deque
import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _  in range(n):
    x = list(map(int,input().strip()))
    graph.append(x)
vis = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
vis[0][0][0] = 1
q = deque()
def bfs(a,b,c):
    q.append((a,b,c))
    while q:
        x,y,z = q.popleft()
        if x == n-1 and y== m-1:
            return vis[x][y][z]
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0<=nx<n and 0<=ny<m:
            #case 1 : 일반적인 bfs
                if vis[nx][ny][z] == 0 and graph[nx][ny] == 0:
                    q.append((nx, ny, z))
                    vis[nx][ny][z] = vis[x][y][z] + 1
            #case 2 : 벽 뚫는 경우 (1) 횟수 남아있고, (2) 벽인경우 (3) 벽뚫고갈곳을 가 봤었는지?
                if graph[nx][ny] == 1 and z < k and vis[nx][ny][z+1] == 0:
                    vis[nx][ny][z+1] = vis[x][y][z] + 1
                    q.append((nx,ny,z+1))
    return -1
ans = bfs(0,0,0)
print(ans)