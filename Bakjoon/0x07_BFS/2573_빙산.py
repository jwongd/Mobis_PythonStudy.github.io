from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
n , m = map(int,input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
flag = 0
day = 0
while True:
    vis = [[0] * m for _ in range(n)]
    zero = [[0] * m for _ in range(n)]
    num = 0
    q = deque()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0 or vis[i][j] != 0:
                continue
            num += 1
            if num > 1:
                flag = 1
                break
            q.append([i,j])
            vis[i][j] = 1
            while q:
                x,y = q.popleft()
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if 0<=nx<n and 0<=ny<m :
                        if board[nx][ny] == 0:
                            zero[x][y] += 1
                        if board[nx][ny] != 0 and vis[nx][ny] == 0:
                            q.append([nx,ny])
                            vis[nx][ny] = 1
    if flag == 1:
        break
    # board = [[max(0,x - 1) for x in row] for row in board]
    for i in range(n):
        for j in range(m):
            board[i][j] -= zero[i][j]
            if board[i][j] < 0:
                board[i][j] = 0
    if sum(sum(row) for row in board) == 0:
        day = 0
        break
    day += 1
print(day)
    #cycle end
