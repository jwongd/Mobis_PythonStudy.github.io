import sys
input = sys.stdin.readline
from collections import deque
q = deque()
m,n,h = map(int,input().split())
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]
a= []
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                q.append((i,j,k))
    a.append(tmp)
while q:
    x,y,z = q.popleft()
    for dir in range(6):
        nx = x + dx[dir]
        ny = y + dy[dir]
        nz = z + dz[dir]
        if 0<= nx < h and 0<= ny < n and 0<=nz < m  and a[nx][ny][nz] == 0 :
            q.append((nx,ny,nz))
            a[nx][ny][nz] = a[x][y][z]+1
mx = -1
for i in a:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        mx = max(mx,max(j))
print(mx-1)





