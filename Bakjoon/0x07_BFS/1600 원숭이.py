from collections import deque
k = int(input())
w,h = map(int,input().split())
vis = [[[0]*(k+1) for _ in range(w)] for _ in range(h)]
vis[0][0][0] = 1
graph = []
q = deque()
for _ in range(h):
    graph.append(list(map(int,input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
dx_horse = [-2,-1,-2,-1,1,1,2,2]
dy_horse = [1,2,-1,-2,2,-2,1,-1]
def bfs():
    q.append((0,0,0))
    while q:
        x,y,z = q.popleft()
        if x == h - 1 and y == w - 1:
            return vis[x][y][z] - 1
        #case 1 . 원숭이 이동
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            nz = z
            if 0<= nx < h and 0<= ny < w :
                if vis[nx][ny][nz] == 0 and graph[nx][ny] == 0:
                    q.append((nx,ny,nz))
                    vis[nx][ny][nz] = vis[x][y][z] + 1
        # case 2 . knight 이동
        if z < k :
            for dir in range(8):
                nx1 = x + dx_horse[dir]
                ny1 = y + dy_horse[dir]
                nz1 = z + 1
                if 0<= nx1 <h and 0<= ny1 < w :
                    if vis[nx1][ny1][nz1] == 0 and graph[nx1][ny1] == 0:
                        q.append((nx1,ny1,nz1))
                        vis[nx1][ny1][nz1] = vis[x][y][z] + 1
    return -1
print(bfs())
