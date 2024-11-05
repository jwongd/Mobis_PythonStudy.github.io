import heapq
from itertools import chain
n = int(input())
graph = [];dx =[-1,1,0,0];dy= [0,0,-1,1]
vis = [[0]*(n+1) for _ in range(n+1)]
for _ in range(n):
    graph.append(list(map(int,input().split())))

q = []
for a in range(n):
    for b in range(n):
        vis[a][b] = 1
        heapq.heappush(q,(-graph[a][b],a,b)) # for 최대 힙
while q:
    cost,x,y = heapq.heappop(q)
    tmp  = []
    for dir in range(4):
        nx,ny = x + dx[dir] , y + dy[dir]
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] > graph[x][y]:
            tmp.append(vis[nx][ny])
    if tmp:
        vis[x][y] = max(tmp) + 1
    else:
        vis[x][y] = 1

print(max(chain(*vis)))