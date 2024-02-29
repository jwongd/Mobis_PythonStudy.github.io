from collections import deque
N = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
board = []
board_rg = []
visit = [[0]*(N+1) for _ in range(N+1)]
visit1 = [[0]*(N+1) for _ in range(N+1)]
for _ in range(N):
    a = list(input())
    board.append(a)
    board_rg.append(a.copy())
for i in range(N):
    for j in range(N):
        if board_rg[i][j] == 'G':
            board_rg[i][j] = 'R'
q = deque()
q1 =deque()
num = 0
num2 = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            q.append((i,j))
            color = board[i][j]
            visit[i][j] = 1
            num += 1
            while q:
                x , y = q.popleft()
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if 0<=nx<N and 0<=ny<N and visit[nx][ny] == 0 :
                        if board[nx][ny]== color:
                            q.append((nx,ny))
                            visit[nx][ny] = 1
#색약
for i in range(N):
    for j in range(N):
        if visit1[i][j] == 0:
            q1.append((i,j))
            color = board_rg[i][j]
            visit1[i][j] = 1
            num2 += 1
            while q1:
                x1 , y1 = q1.popleft()
                for dir in range(4):
                    nx = x1 + dx[dir]
                    ny = y1 + dy[dir]
                    if 0<=nx<N and 0<=ny<N and visit1[nx][ny] == 0 :
                        if board_rg[nx][ny]== color:
                            q1.append((nx,ny))
                            visit1[nx][ny] = 1
print(num, num2)

