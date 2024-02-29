from collections import deque
m,n,h = map(int,input().split())
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
tomato = []
q = deque()
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,input().split())))
    tomato.append(tmp)
# print(*tomato)

for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 1:
                q.append((i,j,k))
# print(q)
while q:
    x,y,z = q.popleft()
    for dir in range(6):
        nx = x + dx[dir]
        ny = y + dy[dir]
        nz = z + dz[dir]
        if 0<= nx < n and 0<=ny<m and 0<=nz<h and tomato[nz][nx][ny] == 0:
            tomato[nz][nx][ny] = tomato[z][x][y] + 1
            q.append((nx,ny,nz))
mx = -1
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)
            mx = max(mx,tomato[i][j][k])
print(mx-1)


