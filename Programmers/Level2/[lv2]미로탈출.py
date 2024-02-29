from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def find(maps):
    col , row = len(maps),len(maps[0])
    for i in range(col):
        for j in range(row):
            if maps[i][j] == 'S':
                start = (i,j)
            if maps[i][j] == 'L':
                lever = (i,j)
    return start,lever
def bfs(st,maps,tg):
    col, row = len(maps), len(maps[0])
    x, y = st
    vis = [[0]*row for _ in range(col)]
    vis[x][y] = 1
    q = deque([(x,y,0)])
    while q:
        x,y,dist = q.popleft()
        if maps[x][y] == tg:
            return dist
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0<=nx<row and 0<=ny<col and not vis[nx][ny] and maps[nx][ny] != 'X':
                vis[nx][ny] = True
                q.append((nx,ny,dist+1))
    return -1
def sol(maps):
    st , lev = find(maps)
    lev_dist = bfs(st,maps,'L')
    end_dist = bfs(lev,maps,'E')
    return lev_dist + end_dist if lev_dist > -1 and end_dist > -1 else -1