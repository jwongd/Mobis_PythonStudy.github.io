from collections import deque
n , m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def BFS(x,y):
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for dir in range(4):
            nx = x+dx[dir]
            ny = y+dy[dir]
            if nx<0 or ny<0 or nx>=n or ny>=m :
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
    return graph[n-1][m-1]

print(BFS(0,0))


