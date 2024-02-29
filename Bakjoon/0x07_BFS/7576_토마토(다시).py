from collections import deque
q = deque()
m,n = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
board = []
visit = [[0]*m for _ in range(n)]

for _ in range(n):
    board.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and visit[i][j]==0:
            q.append((i,j))
            visit[i][j] = 1
while q:
    x , y = q.popleft()
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if nx < 0 or nx >= n or ny < 0 or ny >= m: #이거때메 멈춤
            continue
        if board[nx][ny] != 0 or visit[nx][ny] != 0 :
            continue
        board[nx][ny] = board[x][y] + 1
        visit[nx][ny] = 1
        q.append((nx,ny))

for i in board:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
max = max(map(max,board))
print(max-1)



