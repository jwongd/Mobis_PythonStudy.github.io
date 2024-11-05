from collections import deque
dx = [-1,1,0,0,1,1,-1,-1] ; dy = [0,0,-1,1,1,-1,1,-1]
def bfs(a,b,graph,vis):
    q = deque()
    vis[a][b] = 1
    q.append((a,b))
    while q:
        x,y = q.popleft()
        for dir in range(8):
            nx,ny = x + dx[dir] , y+dy[dir]
            if 0<=nx<h and 0<=ny<w:
                if vis[nx][ny] == 0 and graph[nx][ny]:
                    q.append((nx,ny))
                    vis[nx][ny] = 1
while True:
    w,h = map(int,input().split())
    cnt = 0
    if w == 0 and h == 0: break
    graph = []
    for _ in range(h):
        graph.append(list(map(int,input().split())))
    vis  = [[0] * (w) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if vis[i][j] == 0 and graph[i][j]:
                cnt += 1
                bfs(i,j,graph,vis)
    print(cnt)

