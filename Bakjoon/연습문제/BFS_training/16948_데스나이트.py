N = int(input())
r1,c1,r2,c2 = map(int,input().split())
dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]
board = [[0]*N for _ in range(N)]
from collections import deque
q = deque()
q.append((r1,c1))
while q:
    x,y = q.popleft()
    for dir in range(6):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0<=nx<N and 0<=ny<N:
            if board[nx][ny] == 0:
                board[nx][ny] += board[x][y] + 1
                q.append((nx,ny))
if board[r2][c2] == 0:
    print("-1")
else:
    print(board[r2][c2])
