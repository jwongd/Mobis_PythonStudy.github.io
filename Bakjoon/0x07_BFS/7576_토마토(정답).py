import sys
from collections import deque
input = sys.stdin.readline
m,n = map(int,input().split())
graph = []
queue = deque([])
for i in range(n):
    graph.append(list(map(int,input().split())))

    for j in range(m): #익은 토마토 큐에 저장
        if graph[i][j] == 1:
            queue.append([i,j])
            
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    while queue:
        x,y = queue.popleft()
        for dir in range(4):
            nx = x+ dx[dir]
            ny = y+ dy[dir]
            if 0<= nx < n and 0<=ny<m and graph[nx][ny] == 0 :
                queue.append([nx,ny])
                graph[nx][ny] = graph[x][y] +1
bfs()
ans = 0
for i in graph:
    for j in i:
        if j == 0 :
            print(-1)
            break
    ans = max(ans,max(i))
print(ans-1)


