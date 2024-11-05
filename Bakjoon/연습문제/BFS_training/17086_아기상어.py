N,M = map(int,input().split())
from collections import deque
graph = []
aa = -1
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
for _ in range(N):
    graph.append(list(map(int,input().split())))
q = deque()
def bfs():
    while q:
        x,y = q.popleft()
        for dir in range(8):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 :
            q.append((i,j))
bfs()
print(max(map(max,graph))-1)





