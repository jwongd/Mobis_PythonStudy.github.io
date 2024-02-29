from collections import deque
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
while True:
    l,r,c = map(int,input().split())
    q = deque()
    if l == 0 and r == 0 and c == 0:
        break
    building = []
    vis = [[[0]*c for _ in range(r)] for _ in range(l)]
    mx = -1
    for i in range(l):
        tmp = []
        for j in range(r):
            tmp.append(list(input()))
        building.append(tmp)
        tmp = input() # 한 칸 띄우기
    flag = 0
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == 'S':
                    q.append((i,j,k))
                    vis[i][j][k] = 1
                    while q:
                        if flag == 1:
                            break
                        x,y,z = q.popleft()
                        for dir in range(6):
                            nx = x + dx[dir]
                            ny = y + dy[dir]
                            nz = z + dz[dir]

                            if 0<=nx<l and 0<=ny<r and 0<=nz<c:
                                if building[nx][ny][nz] == 'E':
                                    mx = vis[x][y][z]
                                    flag = 1
                                    break
                                if building[nx][ny][nz] == '.' and vis[nx][ny][nz] == 0:
                                    q.append((nx,ny,nz))
                                    vis[nx][ny][nz] = vis[x][y][z] + 1
    if mx == -1:
        print("Trapped!")
    else:
        print("Escaped in %d minute(s)." % mx)




