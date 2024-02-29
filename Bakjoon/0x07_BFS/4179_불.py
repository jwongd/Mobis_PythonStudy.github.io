from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
r,c = map(int,input().split())
jihoon = deque()
fire = deque()
board = []
visit_jh = [[-1]*c for _ in range(r)]
vis_fire = [[-1]*c for _ in range(r)]
for _ in range(r):
    board.append(list(input()))
#fire
for i in range(r):
    for j in range(c):
        if board[i][j] == 'F':
            fire.append((i, j))
            vis_fire[i][j] = 0
        if board[i][j] == 'J':
            jihoon.append((i,j))
            visit_jh[i][j] = 0

while fire:
    x, y = fire.popleft()
    for dir in range(4):
        nx1 = x + dx[dir]
        ny1 = y + dy[dir]
        if nx1 < 0 or nx1>=r or ny1<0 or ny1>=c:
            continue
        if board[nx1][ny1] == '#' or vis_fire[nx1][ny1] >= 0:
            continue
        vis_fire[nx1][ny1] = vis_fire[x][y] + 1
        fire.append((nx1,ny1))
#jihoon
while jihoon:
    x,y = jihoon.popleft()
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx <0 or nx >= r or ny<0 or ny>=c:
            print(visit_jh[x][y]+1)
            exit(0)
        if board[nx][ny] == '#' or visit_jh[nx][ny] >= 0:
            continue
        if visit_jh[x][y]+1 >= vis_fire[nx][ny] and vis_fire[nx][ny] != -1:
            continue
        visit_jh[nx][ny] = visit_jh[x][y] + 1
        jihoon.append((nx, ny))
print("IMPOSSIBLE")
